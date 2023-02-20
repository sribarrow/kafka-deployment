
"""
    _summary_
"""
import json
import requests
import time
import asyncio
import datetime as dt
from kafka_helper import init_producer
from kafka_helper import produce_record

from config import config
from config import params

# real time data collector
async def async_get_crypto_real_time_data(producer, topic, crypto, time_inverval):
    """
    async_get_crypto_real_time_data _summary_

    Args:
        producer (_type_): _description_
        topic (_type_): _description_
        crypto (_type_): _description_
        time_inverval (_type_): _description_
    """
    while True:
        t_0 = time.time()
        # call API
        header = 'Authorization: Bearer abd90df5f27a7b170cd775abf89d632b350b7c1c9d53e08b340cd9832ce52c2c'
        uri = f"https://api.coinbase.com/v2/prices/{crypto}-{params['ref_currency']}/spot"
        res = requests.get(uri)

        if res.status_code==200:
            # read json response
            raw_data = json.loads(res.content)
            # add schema
            new_data = {
              "timestamp": int(time.time() * 1000),
              "currency": raw_data['data']['base'],
              "amount": float(raw_data['data']['amount'])
            }    
            # produce record to kafka
            produce_record(new_data, producer, topic)
            print(f'Record: {new_data}')
        else:
            # debug / print message
            print('Failed API request at time {dt.datetime.utcnow()}')
        # wait
        await asyncio.sleep(time_inverval - (time.time() - t_0))

# initialize kafka producer
producer = init_producer()

# define async routine
async def main():
    """
    main _summary_
    """
    await asyncio.gather(
    async_get_crypto_real_time_data(producer, config['topic_1'],
                                    params['currency_1'],
                                    params['api_call_period']),
    async_get_crypto_real_time_data(producer, config['topic_2'],
                                    params['currency_2'],
                                    params['api_call_period']),
    async_get_crypto_real_time_data(producer, config['topic_3'],
                                    params['currency_3'],
                                    params['api_call_period'])
)
# run async routine
asyncio.run(main())
