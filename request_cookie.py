#coding:utf-8
#获取响应中得cookies
import requests
url = 'http://www.baidu.com'
response = requests.get(url,allow_redirects=False)#允许重定向
print response.history
print response.status_code
print response.cookies
