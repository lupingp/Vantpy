# -*- coding: utf-8 -*-
# @Time    : 2018/11/14  15:37
# @Author  : 陆平！！
# @FileName: rusi_object_xtjk.py
# @Software: PyCharm

import time
from selenium.webdriver.common.by import By
from aicc_Cloud.aicc_Project.aicc_Page.ruisi_Page import Page

class xtjk_page(Page):
    '''
     ================================定义基本元素,元祖=================================
    '''
    # 定义进入系统监控页面 元素
    xitong_jiankong = (By.CLASS_NAME, 'system')
    '''
     ================================定义基本元素,元祖 方法=================================
    '''
    def xitong_jiankong_log(self):
        #定义进入系统监控页面 元素方法
        self.find_element(*self.xitong_jiankong).click()
    '''
     ================================定义错误元素,元祖=================================
    '''

    '''
    ================================定义错误元素,元祖 方法=================================
    '''