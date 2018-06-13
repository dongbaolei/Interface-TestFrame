# -*- coding:utf-8 -*-
"""
@Time:2018/5/29 14:46
@Author:dongbaolei
"""
import json
import unittest

import requests


# 角色-获取角色
class SysRolePage(unittest.TestCase):
    def setUp(self):
        pass

    def test_sysRolepage(self):
        url = "http://192.168.2.26:8080/sys/sysrole/page"

        payload = {
            "roleName": "1",
            "systemCode": "01"
        }
        headers = {
            'access_token': "2ac5a592-774b-46a3-ad2c-3c27f2a17450",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        print(response.text)
        #print(response.json()['code'])
        self.assertEqual("00", response.json()['code'], msg="00")

    def test_errorORnull_sysRolepage(self):
        url = "http://192.168.2.26:8080/sys/sysrole/page"

        payload = {
            "roleName": "10",
            "systemCode": "01"
        }
        headers = {
            'access_token': "2ac5a592-774b-46a3-ad2c-3c27f2a17450",
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

        print(response.text)
        #print(response.json()['code'])
        self.assertEqual(0, response.json()['data']['pages'], msg="0")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
