#!/bin/bash

#Ping script. Will ping every single host in the defined file

hosts="/tmp/ansible/ip_addresses"

for ip in $(cat $hosts)
do
	ping -c1 $ip &> /dev/null
	if [ $? -eq 0 ]
	then
	echo $ip is REACHABLE
	else
	echo $ip is UNREACHABLE!
	fi
done