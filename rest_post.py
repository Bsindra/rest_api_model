import json
import requests

url = 'http://23c1cdb0d58e.ngrok.io' +'/predict'

request_data = json.dumps({'age':42,'salary':40000})
response = requests.post(url,request_data)
print (response.text)
