# -*- coding:utf-8 -*-
"""
@Time:2018-04-26 14:27
@Author:dongbaolei
"""
from selenium import webdriver


class Headless_phantomjs:
    def headless_phantomjs(self):
        driver = webdriver.PhantomJS()
        driver.get("http://www.lianzhongjr.com/")
        return driver.title

if __name__ == '__main__':
    print(Headless_phantomjs().headless_phantomjs())