# -*- coding:utf-8 -*-
"""
@Time:2018/5/28 17:13
@Author:dongbaolei
"""
import json

import requests


def GetUser_token():
    url = "http://192.168.2.26:8080/uaa/adminlogin"

    payload = {"userAccount": "admin", "userPwd": "111111"}
    headers = {
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    return response.json()['data']['accessToken']
