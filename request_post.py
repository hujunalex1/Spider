#coding=utf-8

'''
发送post请求，通过data参数来传递
'''
import requests
url ="http://httpbin.org/post"
data = {'username':'hujun','password':'123456'}
response = requests.post(url,data=data)
print response.text
print response.status_code















