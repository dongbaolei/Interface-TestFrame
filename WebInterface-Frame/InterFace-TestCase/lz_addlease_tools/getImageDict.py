# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 14:39
@Author:dongbaolei
"""
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')
import json
import requests
import Get_Token
import tools_params

#保存车辆信息
class getImageDict():

    def get_ImageDict(self):
        url = "http://192.168.2.26:8080/lease/image/getImageDict"
        print(tools_params.tools_params().params_getImageDict())
        response = requests.request("POST", url, data=json.dumps(tools_params.tools_params().params_getImageDict()), headers=Get_Token.Get_Token().get_headers())
        return response.json()


if __name__ == '__main__':
    hh = getImageDict()
    print(hh.get_ImageDict())

