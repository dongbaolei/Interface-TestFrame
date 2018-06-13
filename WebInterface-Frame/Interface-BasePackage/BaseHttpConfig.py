# -*- coding:utf-8 -*-
"""
@Time:2018/1/26 13:28
@Author:dongbaolei
"""


class BaseHttpConfig:
    def __init__(self):
        self.timeout = None
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.str = None

    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url

    def set_headers(self, header):
        self.headers = header

    def get_headers(self):
        return self.headers

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_files(self, file):
        self.files = file

    def get_files(self):
        return self.files

    def set_timeout(self, timeout):
        self.str = timeout

    def get_timeout(self):
        return self.timeout
