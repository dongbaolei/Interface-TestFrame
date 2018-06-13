# -*- coding:utf-8 -*-
"""
@Time:2018-04-16 14:29
@Author:dongbaolei
"""
import json
import time

import requests

import getCarID
import getClaim
from getMysqlAppCode import getMysqlAppCode


class FirstAppr:
    appcode = getMysqlAppCode().get_defineAppCode()

    headers = {
        'content-type': "application/json",
        'userid': "1",
        'username': "admin",
        'truename': "admin",
        'cache-control': "no-cache",
    }

    def saveEvaluation(self):
        print("&&&&&&&")
        # print(self.appcode)"appCode": self.appcode,
        carID = getCarID.GetCarID().getCarID(self.appcode)
        saveEvaluation_params = {"id": carID,
                                 "appCode": self.appcode,
                                 "carBrand": "BAW", "carSeries": "BJ212",
                                 "carYear": "(2015-2016) 2015款 快拆蓬型", "carGearBox": "手动", "carDiston": " 2.0L",
                                 "carStyles": "2015款 快拆蓬型 旅行车 5门 手动 5速 四轮驱动 2.0多点式喷射-市场价 61100", "carNewPrice": 61100,
                                 "carIdentify": "WDCBB8GB6BA676906", "engineNo": "943F001796", "carColor": "粉红色",
                                 "interiorColor": "其他", "isOld": "1", "carMiles": 200,
                                 "carFirstBook": "2017-04-15T16:00:00.000Z", "releaseDate": "2017-04-15T16:00:00.000Z",
                                 "carUsage": "02", "carriage": 1, "door": 1, "seat": 3, "evaluatePrice": "58000",
                                 "networkPrice": 6110, "carloanAmount": "11100", "plateNumber": "黑AF6655",
                                 "createTime": "2018-04-17 10:43:22", "updateTime": "2018-04-17 10:43:22",
                                 "bodyColor": "粉红色"}

        response = requests.request("POST", "http://192.168.2.26:8080/appr/lease/appInfo/saveEvaluation",
                                    data=json.dumps(saveEvaluation_params),
                                    headers=self.headers)
        print(response.text)
        return response.text

    def submitFirst(self):
        print("**************")

        submitFirst_params = {
            "loanInfo": {
                "appCode": self.appcode
            },
            "approvalInfo": {
                "action": "kz_pass",
                "reason": "kz_pass_01",
                "reason": "材料齐全，客户诚信，建议批复",
                "remark": "资料无误，通过",
                "nodeCode": "FRAP"}
        }
        response = requests.request("POST", "http://192.168.2.26:8080/appr/lease/approval/submitFirst",
                                    data=json.dumps(submitFirst_params),
                                    headers=self.headers)
        print(9999999)
        print(response.text)
        return response.text


if __name__ == '__main__':
    getClaim.GetClaim().getclaim()
    FirstAppr().saveEvaluation()
    time.sleep(3)
    FirstAppr().submitFirst()
