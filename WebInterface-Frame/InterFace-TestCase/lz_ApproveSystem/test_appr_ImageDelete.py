# -*- coding:utf-8 -*-
"""
@Time:2018-04-04 11:18
@Author:dongbaolei
"""

import os
import sys
import unittest

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


class Appr_ImageDelete(unittest.TestCase):
    def setUp(self):
        self.jira = JiraUtil.JiraUtil()
        pass

    def test_A_right_imagedelete(self):
        '''获取图片小类-输入正确参数'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'lz_ApproveSystem.xlsx', 'approve')
        httpconf.set_url(params[5][2])
        httpconf.set_headers(params[5][3])
        httpconf.set_data(params[5][4])
        # rp = basehttp.post(httpconf.get_url(),eval(httpconf.get_headers()), httpconf.get_data(),
        #                    httpconf.get_files(),
        #                    httpconf.get_timeout())
        # response = requests.request("POST", httpconf.get_url(), data=httpconf.get_data(), headers=eval(httpconf.get_headers()))
        rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
                         httpconf.get_timeout())
        print(rp.json()['message'])
        #self.assertEqual(400, rp.json()['status'], msg='400错误!')


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
