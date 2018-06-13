# -*- coding:utf-8 -*-
"""
@Time:2018-04-10 16:02
@Author:dongbaolei
"""

import DataBaseUtil
from getMysqlAppCode import getMysqlAppCode
from saveCarInfo import saveCarInfo
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')


class getMysqlCarID:
    mydb = DataBaseUtil.DataBaseUtil()
    params1 = saveCarInfo().save_carInfo()
    params =getMysqlAppCode().getAppCode()

    def getCarID(self):
        #print(self.params)
        cc = self.mydb.executeSQL("select id from ca_car_info where app_code='%s'" % self.params)
        carID = self.mydb.get_one(cc)
        print(carID['id'])
        return carID['id']


if __name__ == '__main__':
    print(getMysqlCarID().getCarID())
