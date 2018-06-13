# -*- coding:utf-8 -*-
"""
@Time:2018/6/1 13:42
@Author:dongbaolei
"""

import json
import unittest

import requests

# 编辑车型
class FastCarTypeUpdate(unittest.TestCase):
    def setUp(self):
        pass

    def test_fastCarTypeUpdate(self):
        url = "http://192.168.2.26:8080/fastcar/saleCar/updateCarModel"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
        "carBrand": "法拉利",
        "carImages": [
            {
                "id": 12,
                "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f3d",
                "imageCode": "CAR_IMG_LEFT_FORWARD_45",
                "imageName": "车身照片-左前45°"
            },
            {
                "id": 13,
                "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f4d",
                "imageCode": "CAR_IMG_LEFT",
                "imageName": "车身照片-左侧面"
            }
        ],
        "carModel": "2013款 起亚K3 1.6L 手动GLS 手动 1.6L",
        "carModelCode": "C201805241515071382522",
        "carSeries": "K5",
        "carStoreType": "1",
        "introduces": [
            {
                "carModelCode": "C201805241515071382522",
                "content": "啦啦啦啦",
                "id": 15
            }
        ]
    }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("ok", response.json()['message'], msg="ok")

    def test_paramError_fastCarTypeUpdate(self):
        url = "http://192.168.2.26:8080/fastcar/saleCar/updateCarModel"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
        }
        payload = {
        "carBrand": "法拉利",
        "carImages": [
            {
                "id": 12,
                "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f3d",
                "imageCode": "CAR_IMG_LEFT_FORWARD_45",
                "imageName": "车身照片-左前45°"
            },
            {
                "id": 13,
                "imageAddr": "bb8f2a7d-4b27-4615-a31d-c41172d96f4d",
                "imageCode": "CAR_IMG_LEFT",
                "imageName": "车身照片-左侧面"
            }
        ],
        "carModel": "2013款 起亚K3 1.6L 手动GLS 手动 1.6L",
        "carModelCode": "",
        "carSeries": "K5",
        "carStoreType": "1",
        "introduces": [
            {
                "carModelCode": "C201805241515071382522",
                "content": "啦啦啦啦",
                "id": 15
            }
        ]
    }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        print(response.json()['message'])
        self.assertEqual("传入的车型码没有找到对应的车型", response.json()['message'], msg="传入的车型码没有找到对应的车型")


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
