import pandas as pd 
import numpy as np 
import datetime as dt

from kafka_helper import produce_record, consume_record, init_consumer, init_producer
from config import config, params

# initialize Kafka consumers and producer
print('Starting Apache Kafka consumers and producer')
consumer_1 = init_consumer(config['topic_1'])
consumer_2 = init_consumer(config['topic_2'])
consumer_3 = init_consumer(config['topic_3'])
producer = init_producer()

# intialize local dataframe
data_1 = pd.DataFrame(columns=['time', 'value'])
data_2 = pd.DataFrame(columns=['time', 'value'])
data_3 = pd.DataFrame(columns=['time', 'value'])

while True:
    # consume data from Kafka
    # topic 1 --> 4
    records_1 = consume_record(consumer_1)
    print(f"Consume record from topic \'{config['topic_1']}\' at time {dt.datetime.utcnow()}'")
    for r in records_1:
        dt_obj = dt.datetime.utcfromtimestamp(int(r['timestamp']/1000)).strftime('%Y-%m-%d %H:%M:%S')
        dt_obj = dt.datetime.strptime(dt_obj, '%Y-%m-%d %H:%M:%S')
        # print(dt_obj)
        data_1.loc[len(data_1)] = [int(dt_obj.timestamp() * 1000), float(r['amount'])]
        ma_1 = {'timestamp': r['timestamp'], 'amount': float(data_1['value'].tail(n=params['ma']).mean())}
        # # produce data
        produce_record(ma_1, producer, config['topic_4'])
        print(f"Produce record to topic \'{config['topic_4']}\' at time {dt.datetime.utcnow()}")
    
    # topic 2 --> 5
    records_2 = consume_record(consumer_2)
    print(f"Consume record from topic \'{config['topic_2']}\' at time {dt.datetime.utcnow()}'")
    for r in records_2:
        dt_obj = dt.datetime.utcfromtimestamp(int(r['timestamp']/1000)).strftime('%Y-%m-%d %H:%M:%S')
        dt_obj = dt.datetime.strptime(dt_obj, '%Y-%m-%d %H:%M:%S')
        # dt_obj = dt.datetime.strptime(r['payload']['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        data_2.loc[len(data_2)] = [int(dt_obj.timestamp() * 1000), float(r['amount'])]
        ma_2 = {'timestamp': r['timestamp'], 'amount': float(data_2['value'].tail(n=params['ma']).mean())}
        # produce data
        produce_record(ma_2, producer, config['topic_5'])
        print(f"Produce record to topic \'{config['topic_5']}\' at time {dt.datetime.utcnow()}")

    # topic 3 --> 6
    records_3 = consume_record(consumer_3)
    print(f"Consume record from topic \'{config['topic_3']}\' at time {dt.datetime.utcnow()}'")
    for r in records_3:
        dt_obj = dt.datetime.utcfromtimestamp(int(r['timestamp']/1000)).strftime('%Y-%m-%d %H:%M:%S')
        dt_obj = dt.datetime.strptime(dt_obj, '%Y-%m-%d %H:%M:%S')
        # dt_obj = dt.datetime.strptime(r['payload']['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        data_3.loc[len(data_3)] = [int(dt_obj.timestamp() * 1000), float(r['amount'])]
        ma_3 = {'timestamp': r['timestamp'], 'amount': float(data_3['value'].tail(n=params['ma']).mean())}
        # produce data
        produce_record(ma_3, producer, config['topic_6'])
        print(f"Produce record to topic \'{config['topic_6']}\' at time {dt.datetime.utcnow()}")
