# -*- coding:utf-8 -*-
"""
@Time:2018/1/26 11:34
@Author:dongbaolei
"""
import json

import requests

import BaseHttpConfig


class BaseHttp:
    # defined http get method
    def get(self,url,params,headers,timeout):
        try:
            s = requests.Session()
            response = s.get(url, params=params, headers=headers, timeout=timeout)
            # get请求方式
            # response = requests.request("GET", self.url, headers=self.headers)
            # response.raise_for_status()
            return response
        except RuntimeError:
            # self.logger.error("Time out!")3
            # print "time out"
            return None

    # defined http put method
    def put(self,url,headers):
        try:
            response = requests.request("PUT", url, headers=headers)
            return response
        except RuntimeError:
            # self.logger.error("Time out!")3
            # print "time out"
            return None

    # defined http post method
    def post(self,url,headers,data,files,timeout):
        try:
            s = requests.Session()
            response = s.post(url, headers=headers, data=data, files=files, timeout=timeout)
            # response = requests.post(self.url, data=json.dumps({'model':'user','action':'logon'}))
            # response.raise_for_status()
            return response
        except RuntimeError:
            # self.logger.error("Time out!")
            # print "time out"
            return None


if __name__ == '__main__':
    # post验证
    conf = BaseHttpConfig.BaseHttpConfig()
    conf.set_url('http://192.168.2.122:8081/lzjrapi/loanapply/login')
    data = json.dumps({"userName": "yaogz", "userPassword": "admin2"})
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    conf.set_data(data)
    conf.set_headers(headers)
    pt = BaseHttp()
    #r=pt.post(conf.get_url(),conf.get_headers(),conf.get_data(),conf.get_files(),conf.get_timeout())
    r=pt.get(conf.get_url(),conf.get_data(),conf.get_headers(),conf.get_timeout())

    print(r.status_code)
    s = r.json()
    print (s["data"]["userInfo"]["token"])
    # print (s["code"])
    # print (s["message"])
    # print (s["data"])

    # get 验证
    # url = "http://192.168.2.122:8081/lzjrapi/loanapply/appInfo/getTodayCount"
    #
    # headers = {
    #     'token': s["data"]["userInfo"]["token"],
    #     'cache-control': "no-cache",
    # }
    # response = requests.request("GET", url, headers=headers)
    # print(response.text)
