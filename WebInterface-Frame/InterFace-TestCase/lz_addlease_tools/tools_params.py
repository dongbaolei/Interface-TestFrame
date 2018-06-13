# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 14:40
@Author:dongbaolei
"""
from getMysqlAppCode import getMysqlAppCode
from getMysqlCarID import getMysqlCarID
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')


class tools_params():
    getappcode = getMysqlAppCode().getAppCode()
    getCarID = getMysqlCarID().getCarID()

    # def params_savaAppinfo(self):
    #     params = {
    #         "appInfo": {
    #             "dealerCode": 50000008,
    #             "dealerName": "大发二手车行2",
    #             "productCode": "CTKR",
    #             "productName": "传统库融"
    #
    #         },
    #         "loanInfo": {
    #             "loanAmount": 0,
    #             "loanPeriods": "2"
    #         }
    #     }
    #     return params

    # def params_saveCarInfo(self):
    #     params = {
    #         "appCode": self.getappcode,
    #         "isLcv": "0",
    #         "isOld": "1",
    #         "carBrand": "B 本田",
    #         "carSeries": "理念S1",
    #         "carYear": "(2014-至今) 2014款",
    #         "carGearBox": "手动",
    #         "carDiston": "1.3L",
    #         "carType": "",
    #         "carStyles": "2014款 三厢轿车 4门 舒适版 手动 5速 前轮驱动 1.3多点式喷-市场价 67800",
    #         "carIdentify": "LBEMDAFC3EZ324914",
    #         "carColor": "白色",
    #         "carMiles": 4000,
    #         "carFirstBook": "2015-08-12",
    #         "carSaleName": ":扯呼5姓名",
    #         "carSaleIdno": "1234454",
    #         "carNewPrice": 67800,
    #         "engineNo": "WA320236"
    #     }
    #     return params

    def params_getImageDict(self):
        params = {
            "carId": self.getCarID,
            "appCode": self.getappcode,
            "level1Type": "1"
        }
        return params

    def get_SubImageDict(self):
        params = {
            "appCode": self.getappcode,
            "carId": self.getCarID,
            "level1Type": "01",
            "level2Type": "601"
        }
        return params

    def get_leaseSubmit(self):
        params = {"appCode": self.getappcode}
        return params


if __name__ == '__main__':
    hh = tools_params().get_SubImageDict()
    print(hh)
