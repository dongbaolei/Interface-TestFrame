# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 14:01
@Author:dongbaolei
"""
import json
import unittest

import requests


class sys_UserLogin(unittest.TestCase):
    def setUp(self):
        pass

    def test_login(self):
        '''正确登录'''

        url = "http://192.168.2.26:8080/uaa/adminlogin"

        payload = {"userAccount": "admin", "userPwd": "111111"}
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        print(response.json()['data']['userCode'])
        self.assertEqual("A00001", response.json()['data']['userCode'], msg="登录成功")
        return response.json()['data']['accessToken']

    def test_error_login(self):
        '''错误登录'''

        url = "http://192.168.2.26:8080/uaa/adminlogin"

        payload = {"userAccount": "18516279770", "userPwd": "111111"}
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("登录账户/密码错误", response.json()['message'], msg="登录账户/密码错误")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
