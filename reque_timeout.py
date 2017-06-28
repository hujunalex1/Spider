#coding:utf-8
#使用timeout参数设置超时时间
import requests
response = requests.get('http://www.github.com',timeout=5)#time较小就会出错
print response.status_code
print response.text
