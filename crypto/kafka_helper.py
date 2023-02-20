"""
    _summary_
"""
import json
import datetime as dt
from config import config
from kafka import KafkaProducer
from kafka import KafkaConsumer


def init_producer():
    """
    init_producer _summary_

    Returns:
        _type_: _description_
    """
    # init an instance of KafkaProducer
    print(f'Initializing Kafka producer at {dt.datetime.utcnow()}')
    producer = KafkaProducer(
      bootstrap_servers=config['kafka_broker'],
      value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print(f'Initialized Kafka producer at {dt.datetime.utcnow()}')
    return producer


def produce_record(data, producer, topic, partition=0):
    """
    produce_record _summary_

    Returns:
        _type_: _description_
    """
    # act as a producer sending records on kafka
    print(topic, partition, data)
    producer.send(topic=topic, partition=partition, value=data)
    # debug \ message in prompt
    # print(f"Produce record to topic \'{topic}\' at time {dt.datetime.utcnow()}")
    

def init_consumer(topic, timeout=1000):
    """
    init_consumer _summary_

    Returns:
        _type_: _description_
    """
    # init an instance of KafkaConsumer
    consumer = KafkaConsumer(topic, bootstrap_servers=config['kafka_broker'], group_id=None,
        auto_offset_reset='earliest', enable_auto_commit=False, consumer_timeout_ms=timeout,
        value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    return consumer

def consume_record(consumer):
    """
    consume_record _summary_

    Returns:
        _type_: _description_
    """
    rec_list = []
    # append to list any new records in consumer
    for rec in consumer:
        r = rec.value
        rec_list.append(r)
    # return list of new records
    return rec_list