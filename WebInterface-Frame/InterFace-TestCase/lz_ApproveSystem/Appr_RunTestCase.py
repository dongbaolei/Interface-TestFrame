# -*- coding:utf-8 -*-
"""
@Time:2018/2/1 16:04
@Author:dongbaolei
"""

# discover 方法启动测试脚本


import os
import smtplib
import sys
import time
import unittest
from io import IOBase

import HTMLTestRunnerMH

sys.path.append('..\InterFace-Util')
sys.path.append('..\InterFace-TestCase')

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Run_All():
    def sendmail(self, filenew):
        # 发送邮件地址
        sender = 'baolei.dong@lianzhongjinrong.cn'
        print(filenew)
        # 接收邮件地址
        receiver = '504883618@qq.com'

        # 群发
        #to_list = ['baolei.dong@lianzhongjinrong.cn', 'zhaoxin.zhao@lianzhongjinrong.cn',
        #           'guozheng.yao@lianzhongjinrong.cn',
         #          'jie.li@lianzhongjinrong.cn', 'binbin.yan@lianzhongjinrong.cn']
        to_list = ['tech@lianzhongjinrong.cn']
        f = open(filenew, 'rb')

        mail_body = f.read()

        # print mail_body
        msg = MIMEMultipart()
        # 发送文本
        puretext = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(puretext)
        # 发送附件
        # xlsxpart = MIMEApplication(f.read(),'base64', 'gb2312')
        # xlsxpart.add_header('Content-Disposition', 'attachment', filename='result.html')
        att = MIMEText(open(filenew, 'rb').read(), 'base64', 'gb2312')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="result.html"'
        msg.attach(att)
        f.close()
        # 定义标题
        msg['Subject'] = u"联众库存融资接口测试报告,请及时修改错误"
        # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
        msg['From'] = 'baolei.dong@lianzhongjinrong.cn'
        smtp = smtplib.SMTP()
        # 连接SMTP服务器，此处用的126的SMTP服务器
        smtp.connect('smtp.lianzhongjinrong.cn')
        # 发送邮件用户名和密码
        username = 'baolei.dong@lianzhongjinrong.cn'
        password = 'Blshiniye1985'
        smtp.login(username, password)
        smtp.sendmail(sender, to_list, msg.as_string())
        smtp.quit()

    def sendreport(self):
        result_dir = 'D:\\InterfaceTestReport\\CarUnion'
        lists = os.listdir(result_dir)
        lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
        os.path.isdir(result_dir + "\\" + fn) else 0)
        # print (u'最新测试生成的报告： ' + lists[-2])
        # 找到最新生成的文件
        file_new = os.path.join(result_dir, lists[-1])
        print(file_new)
        # 调用发邮件模块
        self.sendmail(file_new)

    def create_suite(self):
        testsuit = unittest.TestSuite()
        listdir = 'E:\workspace\StockFinan-Frame\WebInterface-Frame\InterFace-TestCase\lz_ApproveSystem'
        discover = unittest.defaultTestLoader.discover(listdir, 'test_*.py', top_level_dir=None)
        for test_suit in discover:
            for test_case in test_suit:
                testsuit.addTest(test_case)
                print(testsuit)
        return testsuit


if __name__ == '__main__':
    alltestname = Run_All().create_suite()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    filename = "D:\\InterfaceTestReport\\CarUnion\\" + now + 'result.html'
    fp = open(filename, 'wb')
    #IOBase()
    runner = HTMLTestRunnerMH.HTMLTestRunner(stream=fp, title=u'联众库存融资测试报告', description=u'用例执行情况')
    result=runner.run(alltestname)
    print(result.failure_count)
    Run_All().sendreport()
