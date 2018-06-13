# -*- coding:utf-8 -*-
"""
@Time:2018-03-15 9:24
@Author:dongbaolei
"""
import os
import sys
import unittest

import requests
from requests_toolbelt import MultipartEncoder

import test_Contract_Params

pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
print(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')
import BaseHttp
import BaseHttpConfig
import DataParamUtil
import test_Contract_Params

class Images_Upload(unittest.TestCase):
    def setUp(self):
        self.data = test_Contract_Params.ContractParams()
        pass

    def test_ImagesUpload(self):
        '''输入正确参数'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'ContractImages.xlsx', 'contract')
        httpconf.set_url(params[0][2])
        httpconf.set_headers(params[0][3])
        httpconf.set_data(params[0][4])

        data=self.data.modify_upload_params()
        # params = MultipartEncoder(
        #     fields={'privateKey':'17ouGiEAi4lQl0Tvma4dAqEdFZnzNPCE', 'seqNo':'3213211', 'busiSysCode': 'loanApply', 'fileContent': '1111',
        #             'file': (open('E:\\test\\11111.jpg', 'rb'), 'image/jpg')}
        # )
        print(data.content_type)
        headers = {'Content-Type': data.content_type}
        rp = basehttp.post(httpconf.get_url(), headers, data, httpconf.get_files(),
                           httpconf.get_timeout())
        #response = requests.request("POST", httpconf.get_url(), data=params, headers=headers)
        print(rp.json())
        self.assertEqual('请求成功!', rp.json()['message'], msg='请求成功!')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
