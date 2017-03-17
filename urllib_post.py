#coding=utf-8

import urllib
import urllib2

values = {}
values['username'] = "18267200735"
values['[password'] = "hj123456"
data = urllib.urlencode(values)
url="https://login-test.lizi.com/login?service=http://www-test.lizi.com/"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()


