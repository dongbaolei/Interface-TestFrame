# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 14:39
@Author:dongbaolei
"""
import json
import requests
import time

import Get_Token
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')


# 新增库存申请
class saveAppInfo():
    def save_appinfo(self):
        params = {
            "appInfo": {"dealerCode": 50000005, "dealerName": "宜春市鑫海服务汽车销售服务有限公司", "productCode": "Y001", "productName": "一车一结"},
            "loanInfo": {"loanAmount": 500.0, "loanPeriods": "7"}}
        url = "http://192.168.2.26:8080/lease/appInfo/saveAppInfo"
        # print(tools_params.tools_params().params_savaAppinfo())
        headers=Get_Token.Get_Token().get_headers()
        time.sleep(1)
        response = requests.request("POST", url, data=json.dumps(params),
                                    headers=headers)
        print(Get_Token.Get_Token().get_headers())
        return response.json()['data']


if __name__ == '__main__':
    hh = saveAppInfo()
    print(hh.save_appinfo())
