import json
import requests
import sys

url, age, salary = sys.argv[1], sys.argv[2], sys.argv[3]

endpoint = url + '/predict'

request_data = json.dumps({'age':age,'salary':salary})

response = requests.post(endpoint, request_data)
print (response.text)
