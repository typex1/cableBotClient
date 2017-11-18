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

response = requests.post(base_url+'moveMM/'+str(length)+'/0/0', headers=headers)

# switch motors off:
response = requests.delete(base_url+'end')
