# -*- coding: utf-8 -*-
# @Time    : 2018/11/6  10:18
# @Author  : 陆平！！
# @FileName: ruisi_public.py
# @Software: PyCharm

import unittest
from aicc_Cloud.aicc_Project.aicc_Page.BrowserDriver import BrowserDriver

class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 浏览器驱动
        driver = BrowserDriver(cls)
        cls.driver = driver.openbrowser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.refresh()
        cls.driver.quit()




