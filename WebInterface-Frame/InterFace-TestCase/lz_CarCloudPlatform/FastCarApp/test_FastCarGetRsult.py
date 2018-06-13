# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 17:52
@Author:dongbaolei
"""

# 查询车结果
import json
import unittest

import requests


class FastCarGetRsult(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarGetRsult(self):
        url = "http://192.168.2.26:8080/fastcar/salePrice/selectSaleCar"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        data = {
            "carBrand": "宝马",
            "endInitPayment": 0,
            "endMouthFee": 0,
            "page": 1,
            "size": 10,
            "startInitPayment": 0,
            "startMouthFee": 0,
            "storeCode": ""
        }
        response = requests.request("POST", url=url, data=json.dumps(data), headers=headers)
        print(response.json()['message'])
        self.assertEqual("请求成功", response.json()['message'], msg='请求成功')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
