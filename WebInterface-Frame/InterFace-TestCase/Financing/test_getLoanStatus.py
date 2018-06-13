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
        url = "http://192.168.2.26:9090/lzfinance/loan/getLoanStatus"

        querystring = {"appCode": "\"L1710091004300101001\"", "appid": "test"}

        payload = "{\"appid\":\"test\",\n\"sign\":123,\n\"appcode\":\"L18032111001001001\"\n}"
        headers = {
            'cache-control': "no-cache",
            'postman-token': "1f08d702-49b0-dd32-5c4d-55df78841c25"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        print(response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
