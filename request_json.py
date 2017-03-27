#coding:utf-8

import requests
import json
url ="http://httpbin.org/post"
data = {'username':'hujun','password':'123456'}
response = requests.post(url,data=json.dumps(data))
print response.text
#如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常
print response.raise_for_status()
