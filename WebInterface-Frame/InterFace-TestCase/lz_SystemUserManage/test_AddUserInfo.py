# -*- coding:utf-8 -*-
"""
@Time:2018/5/30 10:37
@Author:dongbaolei
"""
import json
import random
import string
import unittest

import requests

import GetUser_token
import ID_Card


class Add_UserInfo(unittest.TestCase):
    def setUp(self):
        area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
        self.id_number = ID_Card.gen_id_card(int(area_code), 22, 1)
        self.randomUserCode = ''.join([random.choice(string.digits) for _ in range(6)])
        # print(self.id_number)

    def test_AddUserInfo(self):
        url = "http://192.168.2.26:8080/sys/sysuser"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {
            "idno": self.id_number,
            "positionId": "1",
            "systemCode": "03",
            "userCode": self.randomUserCode,
            "userEmail": "jdongbaolei@126.com",
            "userMobile": "18516279771",
            "userName": "xiaobao",
            "userSex": 1
        }

        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("成功", response.json()['message'], msg="成功")

    def test_error_modifyUserInfo(self):
        url = "http://192.168.2.26:8080/sys/sysuser"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {
            "idno": self.id_number,
            "positionId": "1",
            "systemCode": "03",
            "userCode": "ZY00030",
            "userEmail": "jdongbaolei@126.com",
            "userMobile": "18516279771",
            "userName": "xiaobao",
            "userSex": 1
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("员工号已使用", response.json()['message'], msg="员工号已使用")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
