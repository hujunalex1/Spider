#coding=utf-8

import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    content=response.read().decode('utf-8')
    pattern = re.compile('(.*?).*?(.*?).*?(.*?)',re.S)
    items = re.findall(pattern,content)
    for item in items:
        print item[0],item[1],item[2]
except urllib2.URLError, e:
    print e.reason
except urllib2.HTTPError,e:
    print e.code
