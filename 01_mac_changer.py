#!/usr/bin/env python

import subprocess

adapterName=input('Adapter Name: ')
mac=input('MAC: XX:XX:XX:XX:XX:XX ')

subprocess.call('ifconfig '+adapterName+' down', shell=True)
subprocess.call('ifconfig '+adapterName+' hw ether '+mac, shell=True)
subprocess.call('ifconfig '+adapterName+' up', shell=True)