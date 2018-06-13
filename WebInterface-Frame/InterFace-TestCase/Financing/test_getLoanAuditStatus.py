# -*- coding:utf-8 -*-
"""
@Time:2018-04-02 18:58
@Author:dongbaolei
"""
import unittest

import requests


class BatchPushApplyLoan(unittest.TestCase):
    def setUp(self):
        pass

    def test_batchpushApplyLoan(self):
        url = "http://192.168.2.26:9090/lzfinance/loan/getLoanAuditStatus"

        querystring = {"appCode": "L18032111001001001", "appid": "test", "sign": "123"}

        payload = "{\n\t\"appCode\":\"L18032111001001001\",\n\t\"appid\":\"test\",\n\t\"sign\":123\n\t\n}"
        headers = {
            'cache-control': "no-cache",
            'postman-token': "e8f84699-031f-b446-b28c-9166ed274201"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        print(response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
