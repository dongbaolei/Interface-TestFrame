# -*- coding:utf-8 -*-
"""
@Time:2018-03-15 9:24
@Author:dongbaolei
"""
import json
import os
import sys
import unittest

import requests

import DataParamUtil

pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
print(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')
import BaseHttp
import BaseHttpConfig
import test_Contract_Params
import JiraUtil


class Sign(unittest.TestCase):
    def setUp(self):
        self.jira = JiraUtil.JiraUtil()
        self.data = test_Contract_Params.ContractParams()
        pass

    def test_A_righte_Sign(self):
        '''输入正确参数'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'ContractImages.xlsx', 'contract')
        httpconf.set_url(params[6][2])
        httpconf.set_headers(params[6][3])
        httpconf.set_data(params[6][4])

        rp = basehttp.post(httpconf.get_url(), eval(httpconf.get_headers()), json.dumps(self.data.modify_sign_params()), httpconf.get_files(),
                         httpconf.get_timeout())
        #response = requests.request("POST", httpconf.get_url(), data=httpconf.get_data(), headers=eval(httpconf.get_headers()))
        #rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
        #                  httpconf.get_timeout())
        print(rp.json()['message'])

        self.assertEqual('请求成功!', rp.json()['message'], msg='请求成功!')

    def test_B_errorparam_Sign(self):
        '''输入错误参数'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'ContractImages.xlsx', 'contract')
        httpconf.set_url(params[6][2])
        httpconf.set_headers(params[6][3])
        httpconf.set_data(params[6][4])
        rp = basehttp.post(httpconf.get_url(), eval(httpconf.get_headers()), httpconf.get_data(), httpconf.get_files(),
                         httpconf.get_timeout())
        # print(httpconf.get_url())
        # print(httpconf.get_headers())
        # print(httpconf.get_data())
        # rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
        #                   httpconf.get_timeout())
        print(rp.json()["message"])
        self.assertEqual('seqNo重复', rp.json()['message'], msg='请求异常!')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
