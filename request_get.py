#coding=utf-8
'''
豆瓣获取某个用户的所有图书收藏信息

'''
import requests #调用requests库0
import json
url = "https://api.douban.com/v2/book/user/ahbei/collections" #访问豆瓣ahbei收藏图书接口的url地址
data= {'status':'read','tag':'小说','rating':'5'}
response = requests.get(url,params=data) #发起一个请求，使用get方法
result = response.text  #读取请求返回的结果
print result #打印返回的结果



