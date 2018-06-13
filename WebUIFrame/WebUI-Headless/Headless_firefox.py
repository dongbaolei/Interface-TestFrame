# -*- coding:utf-8 -*-
"""
@Time:2018-04-26 14:35
@Author:dongbaolei
"""
import time
import unittest

from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":

    options = Options()
    options.add_argument('-headless')
    driver = Firefox(executable_path='E:\chromeDownload\geckodriver\geckodriver', firefox_options=options)
    wait = WebDriverWait(driver, timeout=2)
    driver.get('http://www.baidu.com')
    inputTest = "$('#kw').val('python')"
    clickTest = "$('#su').click()"
    #wait.until(expected.visibility_of_element_located((By.NAME, 'wd'))).send_keys('python' + Keys.ENTER)
    #wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.ENTER)

    #driver.execute_script(inputTest)
    # driver.find_element_by_xpath('//*[@id="su"]').click()
    # driver.execute_script(inputTest)
    # time.sleep(5)
    #driver.execute_script(clickTest)
    driver.save_screenshot('123.png')
    time.sleep(3)
    #unittest.TestCase().assertIn('python', driver.title)
    print(driver.title)
    driver.quit()