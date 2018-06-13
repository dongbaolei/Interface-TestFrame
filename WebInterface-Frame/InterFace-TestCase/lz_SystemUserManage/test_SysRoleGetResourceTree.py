# -*- coding:utf-8 -*-
"""
@Time:2018/5/29 14:46
@Author:dongbaolei
"""
import random
import string
import unittest

import requests

import GetUser_token


# 权限资源-资源树结构结果
class SysRoleGetResourceTree(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRolegetResourceTree(self):
        randID = ''.join([random.choice(string.digits) for _ in range(1)])
        print(randID)
        url = "http://192.168.2.26:8080/sys/sysrescource/tree/" + randID + ""

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['code'])
        self.assertEqual("xxx", response.json()['code'], msg="1")

    def test_errorORnull_sysRolegetResourceTree(self):
        randID = ''.join([random.choice(string.digits) for _ in range(5)])
        print(randID)
        url = "http://192.168.2.26:8080/sys/sysrescource/tree/" + randID + ""

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['message'])
        self.assertEqual("no data", response.json()['message'], msg="no data")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
