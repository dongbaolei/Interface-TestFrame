# -*- coding:utf-8 -*-
"""
@Time:2018-04-08 15:42
@Author:dongbaolei
"""
import getSubImageDict
import getImageDict
import lease_Submit
import saveCarInfo
import saveUpload
import os
import sys
pre_path = os.path.abspath('../../Interface-BasePackage')
sys.path.append(pre_path)
sys.path.append('../../Interface-Util')
sys.path.append('../../Interface-Config')

if __name__ == '__main__':
    #saveCarInfo.saveCarInfo().save_carInfo()
    getSubImageDict.getSubImageDict().get_SubImageDict()
    saveUpload.saveUpload().save_Upload()
    lease_Submit.lease_Submit().lease_submit()