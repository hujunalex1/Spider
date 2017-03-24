#coding:utf-8
#获取响应中得cookies
import requests
url = 'http://www.baidu.com'
response = requests.get(url)
print  response.cookies
