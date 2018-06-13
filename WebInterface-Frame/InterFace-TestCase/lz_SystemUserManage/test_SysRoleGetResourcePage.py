# -*- coding:utf-8 -*-
"""
@Time:2018/5/29 14:46
@Author:dongbaolei
"""
import json
import unittest

import requests

import GetUser_token


# 权限资源-资源分页
class SysRoleGetResourcePage(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRolegetResourcePage(self):
        url = "http://192.168.2.26:8080/sys/sysrescource/page/"

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {
            "available": 1,
            "name": "资源21"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        print(response.json())
        self.assertEqual("00", response.json()['code'], msg="00")

    # def test_errorORnull_sysRolegetResourcePage(self):
    #     url = "http://192.168.2.26:8080/sys/sysrescource/page"
    #
    #     headers = {
    #         'Content-Type': "application/json",
    #         'access_token': GetUser_token.GetUser_token(),
    #         'Cache-Control': "no-cache"
    #     }
    #     payload = {
    #         "available": 1,
    #         "name": ""
    #     }
    #
    #     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    #
    #     print(response.json())
    #     #self.assertEqual("no data", response.json()['message'], msg="no data")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
