# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 17:45
@Author:dongbaolei
"""
import json
import unittest

import requests


# 增加登记人
class FastCarCustomerAdd(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarCustomerAdd(self):
        url = "http://192.168.2.26:8080/fastcar/customerRegister/add"
        data = {
            "carModelCode": "C201805221427189482152",
            "mobile": "18277862178",
            "name": "张三",
            "storeCode": "20001002",
            "storeName": "测试门店2"
        }
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url=url, data=json.dumps(data), headers=headers)
        print(response.json())
        self.assertEqual("请求成功", response.json()['message'], msg='请求成功')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
