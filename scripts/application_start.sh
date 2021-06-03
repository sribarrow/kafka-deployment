#!/usr/bin/bash

export CONFLUENT_HOME=/apps/confluent-5.5.0 
export PATH=$PATH:$CONFLUENT_HOME/bin
cd $CONFLUENT_HOME/bin
echo "`date` checking Status" >> /tmp/kafka_deploy.log
confluent local status >> /tmp/kafka_deploy.log
cd $CONFLUENT_HOME/bin
echo "`pwd` - current directory" >> /tmp/kafka_deploy.log
echo "`date` starting services..." >> /tmp/kafka_deploy.log
confluent local start
sleep 30
echo "`date` checking Status" >> /tmp/kafka_deploy.log
confluent local status >> /tmp/kafka_deploy.log
