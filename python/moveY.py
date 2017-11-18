#!/usr/bin/python

import requests
import time
import json
import random
from sys import argv

if len(argv) < 3:
    print "\nUsage: "+argv[0] + "(raspi or local) (length)"
    exit (1)

if (argv[1] == "raspi"):
	base_url = 'http://192.168.1.104:8080/cableBot/'
else:
	base_url = 'http://localhost:8080/'

length = argv[2]
headers = {'Content-Type': 'application/json'}

#response = requests.post(base_url+'linesURL/1a/3/3/0/17/7/0/185', headers=headers)
response = requests.post(base_url+'linesURL/1a/3/0/0/0/'+str(length)+'/0/185', headers=headers)

#dump line data:	
response = requests.get(base_url+'lines')
print json.dumps(response.json(), indent=2)

print "line processing..."
response = requests.get(base_url+'start')
print "/start response: "+ response.text

# clear all lines:
#response = requests.delete(base_url+'linesClear')

# switch motors off:
response = requests.delete(base_url+'end')
