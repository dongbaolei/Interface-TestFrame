# -*- coding:utf-8 -*-
"""
@Time:2018-03-28 17:43
@Author:dongbaolei
"""
import unittest

import requests


class GetAllOrganizationAndDealer(unittest.TestCase):
    def setUp(self):
        pass

    def test_right_params_GetAllOrganizationAndDealer(self):
        '''获取车商和单位信息'''
        url = "http://192.168.2.122:8088/out/getAllOrganizationAndDealer"
        headers = {
            'cache-control': "no-cache",
        }
        response = requests.request("GET", url, headers=headers)
        print(response.json()["message"])
        self.assertEqual("查询成功", response.json()["message"], msg="查询成功")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
