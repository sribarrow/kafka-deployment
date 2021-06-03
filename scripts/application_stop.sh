#!/usr/bin/bash

INS="echo $CONFLUENT_HOME"
if [ -z ${INS} ];
then
   echo "`date` stopping services..." > /tmp/kafka_deploy.log
  # confluent local stop
  echo "`date` checking Status" >> /tmp/kafka_deploy.log
  # confluent local status >> /tmp/kafka_deploy.log

else
   echo "`date` New deployment..." > /tmp/kafka_deploy.log
fi

