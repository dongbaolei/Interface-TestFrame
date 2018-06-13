# -*- coding:utf-8 -*-
"""
@Time:2018-04-09 10:40
@Author:dongbaolei
"""
import json
import requests
import Get_Token
import tools_params
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')

class lease_Submit:
    def lease_submit(self):
        url = "http://192.168.2.26:8080/lease/apply/submit"

        response = requests.request("GET", url, headers=Get_Token.Get_Token().get_headers(),
                                    params=tools_params.tools_params().get_leaseSubmit())
        print(tools_params.tools_params().get_leaseSubmit())

        return response.json()

if __name__ == '__main__':
    lease_Submit().lease_submit()
