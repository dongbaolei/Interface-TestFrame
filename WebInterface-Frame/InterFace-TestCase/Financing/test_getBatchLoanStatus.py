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
        url = "http://192.168.2.26:9090/lzfinance/loan/getBatchLoanStatus"

        payload = "[{\"appid\":\"test\",\n\"sign\":123,\n\"data\":[\"L1710091004300101001\",\"2\"]\n\n\t\n}]\n"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "71b9f258-b039-d8d0-239a-509e8d47e47b"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
