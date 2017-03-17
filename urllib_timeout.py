#coding=utf-8

import urllib2
request = urllib2.urlopen("http://www.baidu.com",timeout=10)
print  request.read()
