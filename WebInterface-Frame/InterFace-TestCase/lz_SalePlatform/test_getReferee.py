# -*- coding:utf-8 -*-
"""
@Time:2018-03-28 17:43
@Author:dongbaolei
"""
import unittest

import requests


class GetReferee(unittest.TestCase):
    def setUp(self):
        pass

    def test_right_params_GetReferee(self):
        '''获取推荐人'''
        url = "http://192.168.2.122:8088/out/getReferee"
        querystring = {"referralCode": "ZY00500"}
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
