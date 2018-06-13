# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 13:42
@Author:dongbaolei
"""

import json
import unittest

import requests

# 添加车型
class FastCarAddNewCartype(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarAddNewCartype(self):
        url = "http://192.168.2.26:8080/fastcar/saleCar/addNewCarModel"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
            "carBrand": "宝马",
            "carImages": [
                {
                    "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f3d",
                    "imageCode": "CAR_IMG_LEFT_FORWARD_45",
                    "imageName": "车身照片-左前45°"
                },
                {
                    "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f4d",
                    "imageCode": "CAR_IMG_LEFT",
                    "imageName": "车身照片-左侧面"
                }
            ],
            "carModel": "2018款 x6 1.6L 手动GLS 手动 2.6L",
            "carSeries": "x6",
            "carStoreType": "1",
            "carGuidePrice": 66.5,
            "introduces": [
                {
                    "content": "老司机快开车",
                    "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f3d"
                }
            ]
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("ok", response.json()['message'], msg="ok")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
