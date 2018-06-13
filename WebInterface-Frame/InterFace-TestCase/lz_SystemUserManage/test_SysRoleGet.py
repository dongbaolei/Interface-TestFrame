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


# 角色-获取角色
class SysRoleGet(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRoleget(self):
        randID = ''.join([random.choice(string.digits) for _ in range(1)])
        print(randID)
        url = "http://192.168.2.26:8080/sys/sysrole/" + randID + ""

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['data']['createBy'])
        self.assertEqual("A00001", response.json()['data']['createBy'], msg="A00001")

    def test_errorORnull_sysRoleget(self):
        randID = ''.join([random.choice(string.digits) for _ in range(5)])
        print(randID)
        url = "http://192.168.2.26:8080/sys/sysrole/" + randID + ""

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
