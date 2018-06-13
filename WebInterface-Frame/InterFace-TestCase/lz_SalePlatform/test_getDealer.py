# -*- coding:utf-8 -*-
"""
@Time:2018-03-28 17:43
@Author:dongbaolei
"""
import unittest

import requests


class GetDealer(unittest.TestCase):
    def setUp(self):
        pass

    def test_right_params_GetDealer(self):
        '''获取车商信息'''
        url = "http://192.168.2.122:8088/out/getDealer"
        querystring = {"dealerCode": "10002005"}
        headers = {
            'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers,params=querystring)
        print(response.json()["message"])
        self.assertEqual("查询成功", response.json()["message"], msg="查询成功")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
