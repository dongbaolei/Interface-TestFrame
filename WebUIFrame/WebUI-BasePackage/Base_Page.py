# -*- coding:utf-8 -*-
"""
@Time:2018-04-27 11:27
@Author:dongbaolei
"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import MyLog


class BasePage(object):
    def __init__(self, selenium_driver, base_url, page_title):
        # self.options = Options()
        # self.options.add_argument('-headless')
        # self.driver = Firefox(executable_path='E:\chromeDownload\geckodriver\geckodriver', firefox_options=self.options)
        self.driver = selenium_driver
        self.url = base_url
        self.title = page_title
        self.mylog = MyLog.Mylog()

    # 打开页面,并校验链接是否加载正确
    def _open(self, url, page_title):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            # 通过断言输入的title是否在当前title中
            assert page_title in self.driver.title, u'打开页面失败：%s' % url
        except:
            self.mylog.error(u'未能正确打开页面:' + url)

    # 重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.mylog.error(u'找不到元素:' + str(loc))

    # 重写send_keys方法
    def send_keys(self, value, clear=True, *loc):
        try:
            if clear:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.mylog.error(u'输入失败,loc=' + str(loc) + u';value=' + value)

    # 截图
    def img_screenshot(self, img_name):
        try:
            # self.driver.get_screenshot_as_file(+img_name+'.png')
            self.driver.save_screenshot('12212.png')
        except:
            self.mylog.error(u'截图失败：' + img_name)


