# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 13:42
@Author:dongbaolei
"""

import json
import unittest

import requests


# 设置车型上架单位、门店
class FastCarTypeSetDoor(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarTypeSetDoor(self):
        url = "http://192.168.2.26:8080/fastcar/salePrice/addSaleStore"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
            "carModelCode": "C201805241515071382522",
            "stores": [
                {
                    "storeCode": "20001002001",
                    "storeName": "测试经销商"
                },
                {
                    "storeCode": "20001003002",
                    "storeName": "测试经销商2"
                }
            ]
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("ok", response.json()['message'], msg="ok")

    def test_paramError_fastCarTypeSetDoor(self):
        url = "http://192.168.2.26:8080/fastcar/salePrice/addSaleStore"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
            "carModelCode": "C201805241515071382522",
            "stores": [
                {
                    "storeCode": "",
                    "storeName": "测试经销商"
                },
                {
                    "storeCode": "20001003002",
                    "storeName": "测试经销商2"
                }
            ]
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("", response.json()['message'], msg="")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
