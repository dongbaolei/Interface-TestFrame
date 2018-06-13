# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 14:14
@Author:dongbaolei
"""
import unittest

import requests


# 获取车型详情
class FastCarTypeGet(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarTypeGet(self):
        url = "http://192.168.2.26:8080/fastcar/saleCar/C201805241515071382522"

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "894b0914-e7d4-4b8c-a7eb-37ef061b9498"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['message'])
        self.assertEqual("请求成功", response.json()['message'], msg="请求成功")

    def test_paramsError_fastCarTypeGet(self):
        url = "http://192.168.2.26:8080/fastcar/saleCar/1232"

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "894b0914-e7d4-4b8c-a7eb-37ef061b9498"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.json()['message'])
        self.assertEqual("没有找到对应的车型", response.json()['message'], msg="没有找到对应的车型")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
