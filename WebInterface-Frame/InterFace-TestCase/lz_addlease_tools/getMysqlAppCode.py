# -*- coding:utf-8 -*-
"""
@Time:2018-04-10 16:02
@Author:dongbaolei
"""

import os
import sys

import time

import DataBaseUtil
import saveAppInfo

pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')


class getMysqlAppCode:
    mydb = DataBaseUtil.DataBaseUtil()
    params = saveAppInfo.saveAppInfo().save_appinfo()

    def getAppCode(self):
        time.sleep(1)
        cc = self.mydb.executeSQL("select app_code from ca_app_info where app_code='%s'" % self.params)
        app_code = self.mydb.get_one(cc)
        print(app_code['app_code'])
        return app_code['app_code']

    def get_defineAppCode(self):
        cc = self.mydb.executeSQL("select app_code from ca_app_info where dealer_code='50000031' ORDER BY update_time DESC LIMIT 1")
        app_code = self.mydb.get_one(cc)
        print(app_code['app_code'])
        return app_code['app_code']


if __name__ == '__main__':
    print(getMysqlAppCode().getAppCode())
    print(getMysqlAppCode().get_defineAppCode())
