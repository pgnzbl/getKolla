#!/usr/bin/env bash

for LINE in `cat results.txt`
do
	if [[ $LINE =~ "centos-source" ]] && [[ $LINE =~ "stein" ]];
	then
	    echo $LINE;
		docker pull 'kolla/'$LINE;
	fi
done