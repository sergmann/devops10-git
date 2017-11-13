#!/bin/bash

if [ `systemctl -t service| grep sshd| awk '{print $1}'` == "sshd.service" ]
then
#mail -s monitoring
echo "OK!"
fi
