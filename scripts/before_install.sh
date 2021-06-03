#!/usr/bin/bash

#sudo yum list >> tmp/kafka_deploy.log
sudo service codedeploy-agent status >> /tmp/kafka_deploy.log

sudo service codedeploy-agent status >> /tmp/kafka_deploy.log

dirname  = "/apps"
if [ -d $dirname ]; then
    echo "`date` $dirname directory exists" >> /tmp/kafka_deploy.log
else
    echo "`date`  creating $dirname directory" >> /tmp/kafka_deploy.log
    sudo mkdir $dirname
    sudo chmod 777 $dirname
fi

cd /apps
echo "`date` deleting existing folder" >> /tmp/kafka_deploy.log
rm -rf confluent-5.5.0
echo "`pwd`" >> /tmp/kafka_deploy.log
echo "`date` downloading Confluent package" >> /tmp/kafka_deploy.log
wget -0 https://packages.confluent.io/archive/5.5/confluent-5.5.0-2.11.tar.gz
echo "`date` untarring Confluent package" >> /tmp/kafka_deploy.log
tar -xvzf confluent-5.5.0-2.11.tar.gz
echo "`date` setting env variable & PATH" >> /tmp/kafka_deploy.log

