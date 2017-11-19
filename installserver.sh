#!/bin/bash
workserver_path=/srv/workserver
mkdir $workserver_path
# cp workserver.py $workserver_path

cp MsgGenRecv.jar $workserver_path

# install python3-bottle 
apt -y update
apt -y install default-jre
apt -y install openjdk-8-jdk

# create a service
touch /etc/systemd/system/workserver.service
printf '[Unit]\nDescription=workServer Service\nAfter=rc-local.service\n' >> /etc/systemd/system/workserver.service
printf '[Service]\nWorkingDirectory=%s\n' $workserver_path >> /etc/systemd/system/workserver.service


printf 'ExecStart=/usr/bin/java -jar %s/MsgGenRecv.jar receive_messages taskqueue 400\n' $workserver_path >> /etc/systemd/system/workserver.service

printf 'ExecReload=/bin/kill -HUP $MAINPID\nKillMode=process\nRestart=on-failure\n' >> /etc/systemd/system/workserver.service
printf '[Install]\nWantedBy=multi-user.target\nAlias=workserver.service' >> /etc/systemd/system/workserver.service
chmod +x /etc/systemd/system/workserver.service

service workserver start



