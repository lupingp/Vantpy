# -*- coding: utf-8 -*-
# @Time    : 2018/11/10  13:17
# @Author  : 陆平！！
# @FileName: ss.py
# @Software: PyCharm

# import time
#
# now_time = time.asctime(time.localtime(time.time()))
# print(now_time)


import datetime
import time
import os
import unittest
from selenium import webdriver
import yaml
# webdriver_chrome = "E:\SoftwareTesting\guge\chrome64_55.0.2883.75\chromedriver.exe"
# driver = webdriver.Chrome(webdriver_chrome)
# driver.get("http://10.0.0.13:3005/")
# time.sleep(2)
# driver.find_element_by_xpath("//*[@id='views']/div[2]/div/form/div[1]/div/div/input").send_keys("test0012")
# driver.find_element_by_xpath("//*[@id='views']/div[2]/div/form/div[2]/div/div/input").send_keys("111111")
# driver.find_element_by_xpath("//*[@id='views']/div[2]/div/form/div[4]/div/button").click()
# time.sleep(1)
# ele = driver.find_element_by_xpath("//*[@id='scroll']/div/div/h1").text
# print(ele)
# ele.get_attribute("textContent")
# File_Path = os.mkdir("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_image\\image\\1_login_case")
# print(File_Path)

# now_time = datetime.datetime.now()
# c_time = ('当前时间是%r'% now_time.second)
# print(c_time)
# path = os.path.dirname(os.path.abspath('.'))  # 这是获取相对路径的方法
# chrome_driver_path = path + '\driver\chrome64_55.0.2883.75\chromedriver.exe'
# ie_driver_path = path + '/driver/IEDriverServer.exe'
# print(path)

# file_path = os.path.dirname(os.getcwd())
# name_path = file_path + '\\yaml\\browser.yaml'
# print(name_path)
# with open(name_path, 'r') as f:
#     temp = yaml.load(f.read())
#     print(temp)

# os_filename = os.path.dirname(os.path.abspath('.'))
# filename = (os_filename + "\\aicc_Report\\Report" + str(1) + '_testreport.html')
# print(filename)
# aa = os.path.dirname(os.getcwd()) + '\\aicc_Project\\aicc_Case'
# print(aa)
# os_discover = os.path.dirname(os.getcwd())
# report_name = os.path.dirname(os.getcwd()) + '\\report\\'
# print(report_name)
# file_path = os.path.dirname(os.getcwd())
# name_path = file_path + '\\yaml\\browser.yaml'
# print(name_path)
# file_path = os.path.dirname(os.path.abspath('.'))+'\\aicc_image'
# print(file_path)
# file_path = os.path.abspath(os.getcwd()) + '\\aicc_image\\aa'
# now = time.strftime("%Y-%m-%d_%H_%M_%S_")
# screen_name = file_path + now + '.jpg'
# print(screen_name)
to = []
for i in range(20):
    to.append(i)
if 1 != 2:
    print(str(to[0]))
