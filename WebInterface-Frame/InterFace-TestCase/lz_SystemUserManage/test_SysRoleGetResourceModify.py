# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 18:18
@Author:dongbaolei
"""
import json
import unittest

import requests

import GetUser_token


# 权限资源-修改资源
class SysRoleGetResourceModify(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRoleGetResourceModify(self):
        '''正确'''

        url = "http://192.168.2.26:8080/sys/sysrescource"

        payload = {
            "id": 15,
            "available": 1,
            "name": "资源21",
            "parentId": 0,
            "permission": "1",
            "seq": "1",
            "systemCode": "01",
            "type": "1",
            "url": "http://www.baidu.com"
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("ok", response.json()['message'], msg="ok")

    def test_error_sysRoleGetResourceModify(self):
        '''错误'''

        url = "http://192.168.2.26:8080/sys/sysrescource"

        payload = {
            "id": 15,
            "available": 1,
            "name": "资源21",
            "parentId": 0,
            "permission": "1",
            "seq": "1",
            "systemCode": "01",
            "type": "1",
            "url": "http://www.baidu.com"
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("类型为菜单时候，parentId必填且不为零", response.json()['message'], msg="类型为菜单时候，parentId必填且不为零")

    def test_paramsNull_sysRoleGetResourceModify(self):
        '''错误'''

        url = "http://192.168.2.26:8080/sys/sysrescource"

        payload = {
            "id": 15,
            "available": 1,
            "name": "资源21",
            "parentId": 0,
            "permission": "1",
            "seq": "1",
            "systemCode": "01",
            "type": "1",
            "url": ""
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("类型为菜单时候，链接必填", response.json()['message'], msg="类型为菜单时候，链接必填")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
