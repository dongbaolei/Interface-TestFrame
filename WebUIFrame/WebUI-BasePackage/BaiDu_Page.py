# -*- coding:utf-8 -*-
"""
@Time:2018-04-27 14:22
@Author:dongbaolei
"""
from selenium.webdriver.common.by import By

from Base_Page import BasePage


class BaiduPage(BasePage):
    # 进行定位
    keywords_loc = (By.ID, 'kw')
    submit_loc = (By.ID, 'su')

    #   打开页面
    def open(self):
        self._open(self.url, self.title)

    #   输入关键词
    def input_keywords(self, keywords):
        self.find_element(*self.keywords_loc).send_keys(keywords)

    #   点击搜索按钮
    def click_submit(self):
        self.find_element(*self.submit_loc).click()

    def execJs(self, inputTest):
        self.driver.execute_script(inputTest)

    def execClickJs(self, ClickTest):
        self.driver.execute_script(ClickTest)
