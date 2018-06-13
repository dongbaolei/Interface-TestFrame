# -*- coding:utf-8 -*-
"""
@Time:2018-03-15 9:24
@Author:dongbaolei
"""

import os
import sys
import unittest

pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
print(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')
import BaseHttp
import BaseHttpConfig
import DataParamUtil
import JiraUtil


class test_getFunds(unittest.TestCase):
    def setUp(self):
        self.jira = JiraUtil.JiraUtil()
        pass

    def test_righterror_getFunds(self):
        '''输入正确参数'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'Financing.xlsx', 'Finance')
        httpconf.set_url(params[0][2])
        httpconf.set_headers(params[0][3])
        httpconf.set_data(params[0][4])
        # rp = basehttp.post(httpconf.get_url(), eval(httpconf.get_headers()), httpconf.get_data(), httpconf.get_files(),
        #                  httpconf.get_timeout())

        rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
                          httpconf.get_timeout())
        print(rp.json()["msg"])
        # # 查找有没有创建过相同BUG
        # jsonJira = self.jira.searchIssue("project=LZFINECAR and summary ~ 输入正确用户名密码登录失败", 0, 5)
        # # 获取BUG状态码
        # getIssueStatue = self.jira.GetIssueTransitionStatus(jsonJira[0])
        # # 如果之前存在BUG，已经修复，本次判断成功的话进行关闭
        # if rp.json()['message'] == '登录成功!':
        #     print(jsonJira[0])
        #     print(getIssueStatue[0]['id'])
        #     if getIssueStatue[0]['id'] == '701':
        #         # print('zzz')
        #         self.jira.updateTransition(jsonJira[0], 701)
        # # 如果之前的BUG没有修复，重新创建或者将已经存在的BUG重新打开
        # else:
        #     print(jsonJira)
        #     print(getIssueStatue[0]['id'])
        #     # 将BUG状态置成reopen
        #     if getIssueStatue[0]['id'] == '3' or getIssueStatue[0]['id'] == '701':
        #         # print('xxx')
        #         self.jira.updateTransition(jsonJira[0], 3)
        #     else:
        #         # pass
        #         # self.jira.login()
        #         # 创建一个新的BUG
        #         self.jira.createIssue('LZFINECAR', '输入正确用户名密码登录失败', '输入正确用户名密码登录失败', 'zhaozhaoxin')
        #         # self.assertEqual('登录成功!', rp.json()['message'], msg='登陆成功断言!')

        self.assertEqual('操作成功', rp.json()['msg'], msg='操作成功')

    def test_errorparam_getFunds(self):
        '''输入错误参数'''
        httpconf = BaseHttpConfig.BaseHttpConfig()
        dataparam = DataParamUtil.DataParamUtil()
        basehttp = BaseHttp.BaseHttp()
        proDir = os.path.abspath('../..')
        params = dataparam.get_xls(proDir, 'Financing.xlsx', 'Finance')
        httpconf.set_url(params[1][2])
        httpconf.set_headers(params[1][3])
        httpconf.set_data(params[1][4])
        # rp = basehttp.post(httpconf.get_url(), eval(httpconf.get_headers()), httpconf.get_data(), httpconf.get_files(),
        #                  httpconf.get_timeout())
        # print(httpconf.get_url())
        # print(httpconf.get_headers())
        # print(httpconf.get_data())
        rp = basehttp.get(httpconf.get_url(), eval(httpconf.get_data()), eval(httpconf.get_headers()),
                          httpconf.get_timeout())
        print(rp.json()["msg"])
        self.assertEqual('数据不存在', rp.json()['msg'], msg='数据不存在')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main
