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


# 权限资源-资源根列表
class SysRoleGetResourceCatalog(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRolegetResourceCatalog(self):
        randID = ''.join([random.choice(string.digits) for _ in range(1)])
        print(randID)
        url = "http://192.168.2.26:8080/sys/sysrescource/catalog/" + randID + ""

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['code'])
        self.assertEqual("00", response.json()['code'], msg="1")

    def test_errorORnull_sysRolegetResourceCatalog(self):
        randID = ''.join([random.choice(string.digits) for _ in range(5)])
        print(randID)
        url = "http://192.168.2.26:8080/sys/sysrescource/catalog/" + randID + ""

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['code'])
        self.assertEqual("00", response.json()['code'], msg="00")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
