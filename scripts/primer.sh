#!/usr/bin/bash

sudo yum -y update
sudo yum -y install ruby
sudo yum -y install wget
sudo yum -y install java-1.8.0

CODEDEPLOY_BIN="/opt/codedeploy-agent/bin/codedeploy-agent"
$CODEDEPLOY_BIN stop

yum erase codedeploy-agent -y

cd /home/ec2-user

wget https://bucket-name.s3.region-identifier.amazonaws.com/latest/install

chmod +x ./install

sudo ./install auto

sudo ./install auto -v releases/codedeploy-agent-###.rpm

sudo yum list >> tmp/kafka_deploy.log
sudo service codedeploy-agent status >> tmp/kafka_deploy.log