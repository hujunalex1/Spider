#coding=utf-8

import urllib

path = "xxx.png"

url = "http://zhaduixueshe.com/static/pic/discovery.png"
#官方推荐做法，非常快，而且好用
urllib.urlretrieve(url,path)
