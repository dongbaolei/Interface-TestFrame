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


# 组织-获取公司列表
class SysRoleGetCompanyAll(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRoleGetCompanyAll(self):

        url = "http://192.168.2.26:8080/sys/company/all"

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
