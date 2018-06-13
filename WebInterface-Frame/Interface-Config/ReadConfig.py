# -*- coding:utf-8 -*-
"""
@Time:2018/1/26 16:00
@Author:dongbaolei
"""

import codecs
import configparser
import os

proDir = os.path.split(os.path.relpath(__file__))[0]
configpath = os.path.join(proDir, "ConfigFile.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configpath)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configpath, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_email(self, name):
        value = self.cf.get("email", name)
        return value

    def get_http(self, name):
        value = self.cf.get("http", name)
        return value

    def get_db(self, name):
        value = self.cf.get("database", name)
        return value
    def get_jiraUrl(self,name):
        value=self.cf.get("jiraurl",name)
        return value

if __name__ == '__main__':
    rd = ReadConfig()
    print(rd.get_jiraUrl('url'))

