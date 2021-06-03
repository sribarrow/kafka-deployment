#!/bin/bash
$INS = "echo $CONFLUENT_HOME"
echo "`date` stopping services..." >/tmp/kafka_deploy.log
# confluent local stop
echo "`date` checking Status" >> /tmp/kafka_deploy.log
# confluent local status >> /tmp/kafka_deploy.log
