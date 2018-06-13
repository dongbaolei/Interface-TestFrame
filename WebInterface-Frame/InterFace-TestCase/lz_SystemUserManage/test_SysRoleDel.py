# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 18:18
@Author:dongbaolei
"""
import json
import unittest

import requests

import GetUser_token

#角色-删除角色
class sys_RoleDel(unittest.TestCase):
    def setUp(self):
        pass

    def test_DelRole(self):
        '''正确参数'''

        url = "http://192.168.2.26:8080/sys/sysrole/13"

        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }

        response = requests.request("DELETE", url, headers=headers)

        print(response.json()['message'])
        self.assertEqual("请先置无效，再删除", response.json()['message'], msg="请先置无效，再删除")

    # def test_systemCodenull_DelRole(self):
    #     '''错误'''
    #
    #     url = "http://192.168.2.26:8080/sys/sysrole"
    #
    #     payload = {"roleName": "11", "systemCode": " "}
    #
    #     headers = {
    #         'Content-Type': "application/json",
    #         'access_token': GetUser_token.GetUser_token(),
    #         'Cache-Control': "no-cache"
    #     }
    #
    #     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    #
    #     print(response.json()['message'])
    #     self.assertEqual("所属系统编码为空", response.json()['message'], msg="所属系统编码为空")
    #
    # def test_roleNamenull_DelRole(self):
    #     '''错误'''
    #
    #     url = "http://192.168.2.26:8080/sys/sysrole"
    #
    #     payload = {"roleName": " ", "systemCode": "01"}
    #
    #     headers = {
    #         'Content-Type': "application/json",
    #         'access_token': GetUser_token.GetUser_token(),
    #         'Cache-Control': "no-cache"
    #     }
    #
    #     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    #
    #     print(response.json()['message'])
    #     self.assertEqual("角色名称为空", response.json()['message'], msg="角色名称为空")
    #
    # def test_error_DelRole(self):
    #     '''错误'''
    #
    #     url = "http://192.168.2.26:8080/sys/sysrole"
    #
    #     payload = {"roleName": "我曹", "systemCode": "我擦"}
    #
    #     headers = {
    #         'Content-Type': "application/json",
    #         'access_token': GetUser_token.GetUser_token(),
    #         'Cache-Control': "no-cache"
    #     }
    #
    #     response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    #
    #     print(response.json()['message'])
    #     #self.assertEqual("所属系统编码为空", response.json()['message'], msg="所属系统编码为空")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
