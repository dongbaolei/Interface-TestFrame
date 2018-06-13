# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 18:18
@Author:dongbaolei
"""
import json
import unittest

import requests

import GetUser_token

#修改角色
class sys_Role(unittest.TestCase):
    def setUp(self):
        pass

    def test_setRole(self):
        '''正确登录'''

        url = "http://192.168.2.26:8080/sys/sysrole"

        payload = {
            "id":"3",
            "roleName": "11",
            "systemCode": "01"
        }

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("ok", response.json()['message'], msg="ok")

    def test_systemCodenull_setRole(self):
        '''错误'''

        url = "http://192.168.2.26:8080/sys/sysrole"

        payload = {"id":"3","roleName": "11", "systemCode": " "}

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("所属系统编码为空", response.json()['message'], msg="所属系统编码为空")

    def test_roleNamenull_setRole(self):
        '''错误'''

        url = "http://192.168.2.26:8080/sys/sysrole"

        payload = {"id":"3","roleName": "", "systemCode": "01"}

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        self.assertEqual("所属系统编码为空", response.json()['message'], msg="所属系统编码为空")

    def test_error_setRole(self):
        '''错误'''

        url = "http://192.168.2.26:8080/sys/sysrole"

        payload = {"id":"3","roleName": "我曹", "systemCode": "我擦"}

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)

        print(response.json()['message'])
        #self.assertEqual("所属系统编码为空", response.json()['message'], msg="所属系统编码为空")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
