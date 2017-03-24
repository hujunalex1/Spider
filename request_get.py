#coding=utf-8

import requests #调用requests库

url = "http://www.lizi.com" #访问接口的url地址
response = requests.get(url) #发起一个请求，使用get方法
result = response.text  #读取请求返回的结果
print result #打印返回的结果

