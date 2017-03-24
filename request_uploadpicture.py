#coding:utf=8
#上传图片


import requests

url = 'http://httpbin.org/post'
file = {'file':open('xxx.png','rb')}
response = requests.post(url,data=file)
print response.status_code
print response.text
