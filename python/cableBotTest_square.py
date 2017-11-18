#!/usr/bin/python

import requests
import time
import json
import random

#base_url = 'http://localhost:8080/'
base_url = 'http://192.168.1.104:8080/cableBot/'
bulk_count = 10
a = 0
b = 99

headers = {'Content-Type': 'application/json'}
#response = requests.post(base_url+'linesURL/1a/81/101/121/0/12/123/185', headers=headers)
# this line is connected to the end point of the line before:
#response = requests.post(base_url+'linesURL/2a/0/12/123/0/121/1223/185', headers=headers)
#response = requests.post(base_url+'linesURL/3a/81/101/121/0/12/123/185', headers=headers)
#time.sleep(1)

print "now adding square lines..."
w=1000
h=2000
#                                              x y z x y z
response = requests.post(base_url+'linesURL/1a/0/0/0/0/'+str(h)+'/0/185', headers=headers)
response = requests.post(base_url+'linesURL/2a/0/'+str(h)+'/0/'+str(w)+'/'+str(h)+'/0/185', headers=headers)
response = requests.post(base_url+'linesURL/3a/'+str(w)+'/'+str(h)+'/0/'+str(w)+'/0/0/185', headers=headers)
response = requests.post(base_url+'linesURL/4a/'+str(w)+'/0/0/0/0/0/185', headers=headers)

print "line addition done."

#dump line data:	
response = requests.get(base_url+'lines')
print json.dumps(response.json(), indent=2)

print "line processing..."
response = requests.get(base_url+'start')
print "/start response: "+ response.text

# clear all lines:
response = requests.delete(base_url+'linesClear')
# switch motors off:
response = requests.delete(base_url+'end')
