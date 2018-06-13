# -*- coding:utf-8 -*-
"""
@Time:2018/5/29 14:46
@Author:dongbaolei
"""
import unittest

import requests

import GetUser_token


# 用户-通过编码获取用户信息
class SysUserCodeGet(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysUserCodeGet(self):
        url = "http://192.168.2.26:8080/sys/sysuser/ZY00030"

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['data']['companyCode'])
        self.assertEqual("C00001", response.json()['data']['companyCode'], msg="C00001")

    def test_error_sysUserCodeGet(self):
        url = "http://192.168.2.26:8080/sys/sysuser/01"

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
