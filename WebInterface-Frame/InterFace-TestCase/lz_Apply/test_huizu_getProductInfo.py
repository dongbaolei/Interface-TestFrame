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

import Get_Token

pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
print(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')
import BaseHttp
import BaseHttpConfig
import DataParamUtil
import JiraUtil


class Hz_GetProductInfos(unittest.TestCase):
    def setUp(self):
        self.jira = JiraUtil.JiraUtil()
        pass

    # def test_A_right_getProductInfos(self):
    #     '''输入正确参数'''
    #     httpconf = BaseHttpConfig.BaseHttpConfig()
    #     dataparam = DataParamUtil.DataParamUtil()
    #     basehttp = BaseHttp.BaseHttp()
    #     proDir = os.path.abspath('../..')
    #     params = dataparam.get_xls(proDir, 'lz_apply.xlsx', 'lzapply')
    #     httpconf.set_url(params[0][2])
    #     httpconf.set_headers(params[0][3])
    #     httpconf.set_data(params[0][4])
    #     rp = basehttp.post(httpconf.get_url(), Get_Token.Get_Token().get_headers(), httpconf.get_data(), httpconf.get_files(),
    #                      httpconf.get_timeout())
    #     #response = requests.request("POST", httpconf.get_url(), data=httpconf.get_data(), headers=eval(httpconf.get_headers()))
    #     # rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
    #     #                  httpconf.get_timeout())
    #     print(rp.json())
    #     self.assertEqual('请求成功!', rp.json()['message'], msg='请求成功!')

    def test_B_errorparam_getProductInfos(self):
        '''输入newCarPrice为空'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'lz_FinanceProduct.xlsx', 'financeproduct')
        httpconf.set_url(params[1][2])
        httpconf.set_headers(params[1][3])
        httpconf.set_data(params[1][4])
        rp = basehttp.post(httpconf.get_url(), Get_Token.Get_Token().get_headers(), httpconf.get_data(), httpconf.get_files(),
                         httpconf.get_timeout())
        # print(httpconf.get_url())
        # print(eval(httpconf.get_data()))
        # print(httpconf.get_data())
        # rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
        #                   httpconf.get_timeout())
        print(rp.json()["message"])
        self.assertEqual('业务渠道不能为空\n', rp.json()['message'], msg='业务渠道不能为空')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
