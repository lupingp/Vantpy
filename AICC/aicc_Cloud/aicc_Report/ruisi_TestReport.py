# -*- coding: utf-8 -*-
# @Time    : 2018/11/5  17:12
# @Author  : 陆平！！
# @FileName: ruisi_log.py
# @Software: PyCharm

# import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
from aicc_Cloud.report.Runner.HTMLTestRunner3 import HTMLTestRunner
import sys

#-====mm===-==定义发送邮件===mu=em=non
def send_mail (file_new):
    # 获取报告文件
    f = open (file_new, 'rb')
    # 读取报告内容
    mail_body = f.read()
    # 读取后关闭
    f.close ()
    # 定义 内容编码格式
    msg = MIMEText (mail_body, 'html', 'utf-8')
    # 邮件标题
    msg ['Subject'] = Header ("自动化测试报告", 'utf-8')
    # 发送的邮箱
    msg['From'] = '18811730879@163.com'
    smtp= smtplib.SMTP()
    smtp.connect ("smtp.163.com") #发送服务器
    smtp.login ("18811730879@163.com","456caocao")#发送账号密码
    smtp.sendmail ("18811730879@163.com","plu@ling-ban.com",msg.as_string())
    smtp.quit ()
print("邮件准备发送中！")

#======查找测试报告目录,找到最新生成的测试报告文件====
def new_report (aicc_report):
    # 获取路径下的文件
    lists = os.listdir (aicc_report)
    # 按照时间顺序排序
    lists.sort (key=lambda fn: os.path.getmtime (aicc_report + "\\" + fn))
    # 获取最新的
    file_new = os.path.join (aicc_report, lists [-1])
    print (file_new)
    return file_new
print ('邮件发送已发送 !')

#======================测试用例集======================

def report():
    if len(sys.argv) > 1:
        report_name = os.path.dirname(os.getcwd()) + '\\report\\'  + sys.argv[1] + '_result.html'
        print(report_name)
        # report_name = 'E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\report' + sys.argv[1] + '_result.html'
    else:
        now = time.strftime("%Y-%m-%d_%H_%M_%S_")
        # 需要查看每段时间的测试报告，可以这样写：
        report_name = os.path.dirname(os.getcwd()) + '\\report\\'+now+'Rs_html_Report.html'
        print(report_name)
        # report_name = report_name + 'E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\report\\Rs_html_Report.html'
    return report_name


if __name__=="__main__":
    fp = open (report(), 'wb')
    #定义测试报告标题与内容
    runner = HTMLTestRunner(stream=fp,
        title=u'睿思云平台测试报告',description=u"环境: windows 7浏览器: Chrome")
    #批量执行测试Case
    os_discover = os.path.dirname(os.getcwd())
    discover = unittest.defaultTestLoader.discover (os_discover + '\\aicc_Project\\aicc_Case',
                                                    pattern="test_1_login_case.py")
    #执行
    runner.run (discover)
    #关闭生成的报告
    fp.close ()
    #查找新生成的报告
    # os_o = os.path.dirname(os.path.abspath('.'))
    # file_report_path =new_report ('E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\report\\Rs_html_Report.html')
    # send_mail (file_report_path) #调用发邮件模块

