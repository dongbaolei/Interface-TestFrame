# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 17:52
@Author:dongbaolei
"""

# 查询车详情
import unittest

import requests


class FastCarGet(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarGet(self):
        url = "http://192.168.2.26:8080/fastcar/salePrice/getSaleCarDetail/C201805241515071382522"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        response = requests.request("GET", url=url, headers=headers)
        print(response.json()['message'])
        self.assertEqual("请求成功", response.json()['message'], msg='请求成功')

    def tearDown(self):
        pass
