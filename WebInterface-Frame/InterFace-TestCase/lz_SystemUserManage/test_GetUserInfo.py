# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 17:18
@Author:dongbaolei
"""
import unittest

import requests

import GetUser_token


class GetUserInfo(unittest.TestCase):
    def setUp(self):
        pass

    def test_getuserinfo(self):
        url = "http://192.168.2.26:8080/sys/user"

        headers = {
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['data'])
        self.assertEqual("admin", response.json()['data']['userAccount'], msg="admin")

    def test_error_getuserinfo(self):
        url = "http://192.168.2.26:8080/sys/user"

        headers = {
            'access_token': "21212121212121122",
            'Cache-Control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json())
        self.assertEqual("invalid_token", response.json()['error'], msg="invalid_token")

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main
