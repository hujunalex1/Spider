#coding:utf-8

import requests
import json
url ="http://httpbin.org/post"
data = {'username':'hujun','password':'123456'}
response = requests.post(url,data=json.dumps(data))
print response.text
