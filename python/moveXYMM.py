#!/usr/bin/python

import requests
import time
import json
import random
from sys import argv

if len(argv) < 5:
    print "\nUsage: "+argv[0] + " (raspi or local) (x) (y) (stepPause)"
    exit (1)

if (argv[1] == "raspi"):
	base_url = 'http://192.168.1.114:8080/cableBot/'
else:
	base_url = 'http://localhost:8080/'

x = argv[2]
y = argv[3]
stepPause = argv[4]

headers = {'Content-Type': 'application/json'}
Url=base_url+'moveMM/'+str(x)+'/'+str(y)+'/0/'+str(stepPause)
print "Url is "+Url

response = requests.post(Url, headers=headers)

# switch motors off:
response = requests.delete(base_url+'end')
