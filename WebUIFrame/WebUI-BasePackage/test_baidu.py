# -*- coding:utf-8 -*-
"""
@Time:2018-04-27 14:26
@Author:dongbaolei
"""
import unittest
from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver import Chrome
#firefox 方式
#from selenium.webdriver.firefox.options import Options
#chrom方式
from selenium.webdriver.chrome.options import Options

from BaiDu_Page import BaiduPage


class TestBaiduSearch(unittest.TestCase):
    def setUp(self):
        self.options = Options()
        self.options.add_argument('-headless')
        self.options.add_argument('--disable-gpu')
        #chrome需要将chromdriver放到python目录下，不然会报path错误
        self.options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        #self.driver = Firefox(executable_path='E:\chromeDownload\geckodriver\geckodriver', firefox_options=self.options)
        self.driver = Chrome(chrome_options=self.options)
        self.url = 'https://www.baidu.com/'
        self.keyword = 'python'
        self.inputTest = "$('#kw').val('python')"
        self.clickTest = "$('#su').click()"
        self.baidu_page = BaiduPage(self.driver, self.url, u'百度')

    def test_baidu_search(self):
        u'''百度搜索'''
        try:
            self.baidu_page.open()
            # self.baidu_page.input_keywords(self.keyword)
            # self.baidu_page.click_submit()
            self.baidu_page.execJs(self.inputTest)
            self.baidu_page.execClickJs(self.clickTest)

            sleep(5)
            print(self.driver.title)
            # self.assertIn(self.keyword, self.driver.title)

        except Exception as e:
            self.baidu_page.img_screenshot(u'百度搜索')
            raise e

    def test_error_search(self):
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main
