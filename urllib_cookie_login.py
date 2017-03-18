#coding=utf-8

import urllib2
import urllib
import cookielib

filename = "cookie_login.txt"
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建数据，登录网站的用户名及密码
values ={}
values['email'] = "18267200735"
values['password'] = "xxxxx"
#格式化数据
postdata = urllib.urlencode(values)
#imooc网站登录接口url
loginurl = "http://www.imooc.com/user/newlogin"
#进行登录请求
req1 = opener.open(loginurl,postdata)
print req1.read()
#保存登录后的cookie
cookie.save(ignore_expires=True,ignore_discard=True)
#我的课程的url地址
courseurl = "http://www.imooc.com/u/3395674/courses"
#请求我的课程页面
req2 = opener.open(courseurl)
print req2.read()




