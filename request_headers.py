#coding:utf-8
#定制headers
import requests
import json

url = 'http://httpbin.org/post'
data = {'some':'data'}
headers = {'content-type':'application/json'}
response = requests.post(url,data=json.dumps(data),headers=headers)
print response.status_code
print response.text
print response.headers
print response.headers.get('content-type')

