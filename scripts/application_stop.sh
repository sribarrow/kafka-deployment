#!/bin/bash
echo "`date` starting services..." >> /tmp/kafka_deploy.log
confluent local stop
echo "`date` checking Status" >> /tmp/kafka_deploy.log
confluent local status >> /tmp/kafka_deploy.log