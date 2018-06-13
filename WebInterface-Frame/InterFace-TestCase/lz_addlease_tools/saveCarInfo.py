# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 14:39
@Author:dongbaolei
"""
import json
import os
import sys

import requests

import Get_Token
from getMysqlAppCode import getMysqlAppCode

pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')


# 保存车辆信息



class saveCarInfo():
    def save_carInfo(self):
        url = "http://192.168.2.26:8080/lease/appInfo/saveCarInfo"
        params = {
            "appCode": getMysqlAppCode().getAppCode(),
            "carBrand": "北汽制造",
            "carSeries": "BJ 212",
            "carYear": "(2015-2016) 2015款 快拆蓬型",
            "carGearBox": "手动",
            "carDiston": " 2.0L",
            "carStyles": "2015款 快拆蓬型 旅行车 5门 手动 5速 四轮驱动 2.0多点式喷射-市场价 61100",
            "carNewPrice": 61100,
            "carIdentify": "WDCBB8GB6BA676906",
            "engineNo": "943F001796",
            "carColor": "粉红色",
            "interiorColor": "其他",
            "isOld": "1",
            "carMiles": 200,
            "carFirstBook": "2017-04-16 00:00:00",
            "releaseDate": "2017-04-16 00:00:00",
            "carUsage": "02",
            "carriage": 1,
            "door": 1,
            "seat": 3,
            "evaluatePrice": 22.28,
            "networkPrice": 6110,
            "carloanAmount": 111,
            "plateNumber": "黑AF6655",
            "createTime": "2018-04-17 10:27:28",
            "updateTime": "2018-04-17 10:31:30"
        }
        # print(tools_params.tools_params().params_saveCarInfo())
        response = requests.request("POST", url, data=json.dumps(params),
                                    headers=Get_Token.Get_Token().get_headers())
        # print(saveAppInfo.saveAppInfo().save_appinfo())
        return response.json()['data']


if __name__ == '__main__':
    hh = saveCarInfo()
    print(hh.save_carInfo())
