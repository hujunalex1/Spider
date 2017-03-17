#coding=utf-8


import urllib2
import urllib

values={}
values['username'] = "18267200735"
values['password'] = "hj123456"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url+"?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
print geturl




