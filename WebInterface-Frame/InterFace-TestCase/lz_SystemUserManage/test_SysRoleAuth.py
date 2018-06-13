# -*- coding:utf-8 -*-
"""
@Time:2018/5/29 13:35
@Author:dongbaolei
"""
import json
# 角色-授权资源
import unittest

import requests

import GetUser_token


class SysRoleAuth(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRoleAuth(self):
        url = "http://192.168.2.26:8080/sys/sysrole/auth"

        payload = {
            "roleId": "11",
            "resourceIds": [1, 2]
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.text)
        self.assertEqual("ok", response.json()['message'], msg="ok")


    def test_error_sysRoleAuth(self):
        url = "http://192.168.2.26:8080/sys/sysrole/auth"

        payload = {
            "111": "11000",
            "111": [1, 2,3]
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.text)
        self.assertEqual("资源组至少有一个", response.json()['message'], msg="资源组至少有一个")

    def test_roleIdNull_sysRoleAuth(self):
        url = "http://192.168.2.26:8080/sys/sysrole/auth"

        payload = {
            "roleId": "",
            "resourceIds": [1, 2]
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.text)
        self.assertEqual("roleId必填", response.json()['message'], msg="roleId必填")

    def test_resourceIdsNull_sysRoleAuth(self):
        url = "http://192.168.2.26:8080/sys/sysrole/auth"

        payload = {
            "roleId": "11",
            "resourceIds": []
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.text)
        self.assertEqual("资源组至少有一个", response.json()['message'], msg="资源组至少有一个")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
