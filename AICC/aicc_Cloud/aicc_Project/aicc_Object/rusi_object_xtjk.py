# -*- coding: utf-8 -*-
# @Time    : 2018/11/14  15:37
# @Author  : 陆平！！
# @FileName: rusi_object_xtjk.py
# @Software: PyCharm

import time
from selenium.webdriver.common.by import By
from AICC.aicc_Cloud.aicc_common.ruisi_Base import BasePage

class xtjk_page(BasePage):
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
        self.click(self.xitong_jiankong)
    '''
     ================================定义错误元素,元祖=================================
    '''

    '''
    ================================定义错误元素,元祖 方法=================================
    '''