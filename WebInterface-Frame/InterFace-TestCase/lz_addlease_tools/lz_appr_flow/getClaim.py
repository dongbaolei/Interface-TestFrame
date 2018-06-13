# -*- coding:utf-8 -*-
"""
@Time:2018-04-11 17:30
@Author:dongbaolei
"""
import json
import time

import requests

from getMysqlAppCode import getMysqlAppCode
from lz_addlease_tools import getSubImageDict
from lz_addlease_tools import lease_Submit
from lz_addlease_tools import saveUpload


class GetClaim:
    getSubImageDict.getSubImageDict().get_SubImageDict()
    saveUpload.saveUpload().save_Upload()
    # lease_Submit.lease_Submit().lease_submit()
    url = "http://192.168.2.26:8080/appr/lease/approval/claim"
    headers = {
        'content-type': "application/json",
        'userid': "1",
        'username': "admin",
        'truename': "admin",
        'cache-control': "no-cache",
    }
    getclaim_params = {
        "appCode": lease_Submit.lease_Submit().lease_submit()['data'],
        "userId": "1",
        "nodeCode": "FRAP"
    }

    def getclaim(self):
        # FRAP 初审领单
        print(11111)
        print(self.getclaim_params)
        time.sleep(4)
        response = requests.request("POST", self.url, data=json.dumps(self.getclaim_params), headers=self.headers)
        print(response.text)
        return response.json()



if __name__ == '__main__':
    # GetClaim().getclaim()
    GetClaim().getclaim()
    # GetClaim().saveEvaluation()
    # GetClaim().submitFirst()
