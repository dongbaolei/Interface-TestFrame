# -*- coding:utf-8 -*-
"""
@Time:2018/5/30 10:37
@Author:dongbaolei
"""
import json
import random
import unittest

import requests

import GetUser_token
import ID_Card


class Modify_UserInfo(unittest.TestCase):
    def setUp(self):
        area_code = random.choice(["420102", "420103", "420104", "420105", "420106", "420107"])
        self.id_number = ID_Card.gen_id_card(int(area_code), 22, 1)
        # print(self.id_number)

    def test_modifyUserInfo(self):
        url = "http://192.168.2.26:8080/sys/sysuser"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {
            "id": 66,
            "idno": self.id_number,
            "positionId": "1",
            "systemCode": "03",
            "userCode": "ZY00030",
            "userEmail": "jinjin.zheng@126.com",
            "userMobile": "13818764292",
            "userName": "aaa",
            "userSex": 1
        }

        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("ok", response.json()['message'], msg="ok")

    def test_error_modifyUserInfo(self):
        url = "http://192.168.2.26:8080/sys/sysuser"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload = {
            "id": 66888888888,
            "idno": self.id_number,
            "positionId": "1",
            "systemCode": "03",
            "userCode": "ZY00030",
            "userEmail": "jinjin.zheng@126.com",
            "userMobile": "13818764292",
            "userName": "aaa",
            "userSex": 1
        }
        response = requests.request("PUT", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("参数非法", response.json()['message'], msg="参数非法")

    def test_paramNull_modifyUserInfo(self):
        url = "http://192.168.2.26:8080/sys/sysuser"
        headers = {
            'Content-Type': "application/json",
            'access_token': GetUser_token.GetUser_token(),
            'Cache-Control': "no-cache"
        }
        payload_IDnull = {"id": "","idno": self.id_number,"positionId": "1","systemCode": "03","userCode": "ZY00030",
            "userEmail": "jinjin.zheng@126.com",
            "userMobile": "13818764292",
            "userName": "aaa",
            "userSex": 1
        }
        response = requests.request("PUT", url, data=json.dumps(payload_IDnull), headers=headers)
        self.assertEqual("id为空", response.json()['message'], msg="id为空")

        payload_PositionIdnull = {"id": "66", "idno": self.id_number, "positionId": "", "systemCode": "03",
                          "userCode": "ZY00030",
                          "userEmail": "jinjin.zheng@126.com",
                          "userMobile": "13818764292",
                          "userName": "aaa",
                          "userSex": 1
                          }
        response = requests.request("PUT", url, data=json.dumps(payload_PositionIdnull), headers=headers)
        self.assertEqual("岗位为空", response.json()['message'], msg="岗位为空")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
