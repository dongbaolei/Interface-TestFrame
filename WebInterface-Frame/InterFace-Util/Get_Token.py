# -*- coding:utf-8 -*-
"""
@Time:2018-03-27 16:25
@Author:dongbaolei
"""

import requests


class Get_Token():
    def gettoken(self):
        url = "http://192.168.2.122:8081/lzjrapi/loanapply/login"
        payload = "{\n  \"userPassword\" : \"admin2\",\n  \"userName\" : \"L18721648275\"\n}"
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache",
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()['data']['userInfo']['token']

    def get_headers(self):
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'token': self.gettoken()
        }
        return headers


if __name__ == '__main__':
    print(Get_Token().get_headers())
