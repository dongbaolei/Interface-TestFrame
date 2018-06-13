# -*- coding:utf-8 -*-
"""
@Time:2018/1/26 14:15
@Author:dongbaolei
"""
import os
from xml.etree import ElementTree as ElementTree
from xlrd import open_workbook




# 从excel文件中读取测试用例
class DataParamUtil:
    def get_xls(self,proDir,xls_name, sheet_name):
        cls = []
        # get xls file's path
        xlsPath = os.path.join(proDir, "InterFace-DataFile", xls_name)
        #print(xlsPath)
        # open xls file
        file = open_workbook(xlsPath)
        # get sheet by name
        sheet = file.sheet_by_name(sheet_name)
        # get one sheet's rows
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls

if __name__ == '__main__':
    # print get_xls('test.xlsx','test')
    util = DataParamUtil()
    mylist = util.get_xls('Financing.xlsx', 'Finance')
    print(mylist[0][2])
    # print mylist[1][2]
    print(mylist[0][4])
    print(mylist[0][5])

