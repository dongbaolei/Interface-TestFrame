# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 17:34
@Author:dongbaolei
"""
import json
import unittest

import requests

import GetUser_token


class Modify_Userpwd(unittest.TestCase):
    def setUp(self):
        pass

    def test_modifyuserpwd(self):
        url = "http://192.168.2.26:8080/sys/user/modifypwd"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {"oldPwd": "111111", "newPwd": "111111"}
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("成功", response.json()['message'], msg="成功")

    def test_error_modifyuserpwd(self):
        url = "http://192.168.2.26:8080/sys/user/modifypwd"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {"oldPwd": " ", "newPwd": "111111"}
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("旧密码为空", response.json()['message'], msg="旧密码为空")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
