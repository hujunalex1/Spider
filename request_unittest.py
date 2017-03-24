#coding=utf-8

import requests
import unittest
import json

class MyTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://www.imooc.com/user/newlogin"

    def test_get_success(self):
        datalist = {'emali':'1823672007xx','password':'xxxx'}
        head = {"Content-Type": "application/Json"}
        r = requests.post(self.url,params=datalist,headers=head)
        result = json.load(r.text)
        print result

if __name__ == '__main__':
    unittest.main()



