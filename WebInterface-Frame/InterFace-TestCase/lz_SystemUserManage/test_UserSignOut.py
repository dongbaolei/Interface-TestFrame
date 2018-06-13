# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 16:17
@Author:dongbaolei
"""
import unittest

import requests

import GetUser_token


class sys_UserSignOut(unittest.TestCase):
    def setUp(self):
        pass

    def test_signout(self):
        '''退出登录'''
        url = "http://192.168.2.26:8080/uaa/signout"
        headers = {
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, headers=headers)

        print(response.json()['message'])
        self.assertEqual("成功", response.json()['message'], msg="成功")

    def test_error_signout(self):
        '''错误条件退出登录'''
        url = "http://192.168.2.26:8080/uaa/signout"
        headers = {
            'access_token': "21212121212121",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, headers=headers)

        print(response.json()['error'])
        self.assertEqual("invalid_token", response.json()['error'], msg="invalid_token")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.TestCase
