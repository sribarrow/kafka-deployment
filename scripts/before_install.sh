#!/usr/bin/bash

#sudo yum list >> tmp/kafka_deploy.log
sudo service codedeploy-agent status >> tmp/kafka_deploy.log

DIR = "/apps"
if [ -d "${DIR}" ]; then
    echo "`date` ${DIR} directory exists" >> /tmp/kafka_deploy.log
else
    echo "`date`  creating ${DIR} directory" >> /tmp/kafka_deploy.log
    sudo mkdir ${DIR}
    chmod 777 ${DIR}
fi
cd /apps
echo "`date` downloading Confluent package" >> /tmp/kafka_deploy.log
wget https://packages.confluent.io/archive/5.5/confluent-5.5.0-2.11.tar.gz
echo "`date` untarring Confluent package" >> /tmp/kafka_deploy.log
tar -xvzf confluent-5.5.0-2.12.tar.gz
echo "`date` setting env variable & PATH" >> /tmp/kafka_deploy.log
export CONFLUENT_HOME=/apps/confluent-5.5.0
export PATH=$PATH:$CONFLUENT_HOME/bin
cd $CONFLUENT_HOME/bin
echo "`date` checking Status" >> /tmp/kafka_deploy.log
confluent local status >> /tmp/kafka_deploy.log

