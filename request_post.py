#coding=utf-8

import requests
datalist= {}
datalist['email']='18267200732'
datalist['password']='xxxx'
url = "http://www.imooc.com/user/newlogin"
head = {"Content-Type": "application/Json"}

response = requests.post(url,data=datalist,headers=head)

print response.text










