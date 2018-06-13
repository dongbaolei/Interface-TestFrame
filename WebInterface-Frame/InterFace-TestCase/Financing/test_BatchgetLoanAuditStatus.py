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
        url = "http://192.168.2.26:9090/lzfinance/loan/getBatchLoanAuditStatus"

        payload = "[\"\",\"\"]"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
