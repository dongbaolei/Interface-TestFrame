# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 13:17
@Author:dongbaolei
"""
import json
import unittest

import requests


# 获取车型列表
class FastCarTypeList(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarTypeList(self):
        url = "http://192.168.2.26:8080/fastcar/saleCar/page"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
            "carBrand": "起亚",
            "carModel": "",
            "carSeries": "",
            "page": 1,
            "size": 10
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("请求成功", response.json()['message'], msg="请求成功")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main