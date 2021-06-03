#!/usr/bin/bash

cd $CONFLUENT_HOME/bin
echo "`date` starting services..." >> /tmp/kafka_deploy.log
confluent local start
echo "`date` checking Status" >> /tmp/kafka_deploy.log
confluent local status >> /tmp/kafka_deploy.log

