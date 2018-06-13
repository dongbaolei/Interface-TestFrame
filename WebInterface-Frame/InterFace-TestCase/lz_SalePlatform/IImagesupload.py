# -*- coding:utf-8 -*-
"""
@Time:2018-03-29 15:08
@Author:dongbaolei
"""
import unittest

import requests
from requests_toolbelt import MultipartEncoder

import JiraUtil


class KR_Images_Upload(unittest.TestCase):
    def setUp(self):
        self.jira = JiraUtil.JiraUtil()
        pass

    def test_saveUpload(self):
        url = "http://192.168.2.26:9095/lzjrapi/lease/image/saveUpload"

        params = MultipartEncoder(
            fields={'appCode': 'K18031911001001001', 'carId': '1', 'imgCode': 'ncontract_prop_auth',
                    'imgSeq': '100000', 'imgKey': '46349bceee3d413c842e40f12d8b01c2', 'level4Name': '主贷人手持借款服务合同',
                    'level1Type': '4',
                    'file': (open('E:\\test\\11111.jpg', 'rb'), 'image/jpeg')}
        )
        headers = {'Content-Type': params.content_type}

        response = requests.request("POST", url, data=params, headers=headers)
        print(response.json()['message'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
