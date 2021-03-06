# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 13:42
@Author:dongbaolei
"""

import json
import unittest

import requests


# 获取金融方案列表
class FastCarTypeGetSalePriceList(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarTypeGetSalePriceList(self):
        url = "http://192.168.2.26:8080/fastcar/salePrice/getSalePrices"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
            "carModelCode": "C201805221427189482155",
            "storeCode": "20001002"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("请求成功", response.json()['message'], msg="请求成功")

    def test_paramError_fastCarTypeGetSalePriceList(self):
        url = "http://192.168.2.26:8080/fastcar/salePrice/getSalePrices"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
            "carModelCode": "C201805221427189482155",
            "storeCode": "20001002"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("", response.json()['message'], msg="")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
