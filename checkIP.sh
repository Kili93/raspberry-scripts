#!/bin/bash

PUBLIC_IP=`wget http://ipecho.net/plain -O - -q ; echo`
if [ -s currentIP.dat ]; then
        # Read the age from the file.
        CURRENT_IP=`cat currentIP.dat`
        if [ "$PUBLIC_IP" == "$CURRENT_IP" ]; then
                echo ''
        else
                echo $PUBLIC_IP > currentIP.dat
                cat msg.txt | sed -e "s/NEWIPADDRESS/$PUBLIC_IP/" >> msg.txt
                ssmtp kilian.bissig@hotmail.com  < msg.txt
        fi
fi

