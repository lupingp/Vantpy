# -*- coding: utf-8 -*-
# @Time    : 2018/11/14  15:25
# @Author  : 陆平！！
# @FileName: rusi_object_whrw.py
# @Software: PyCharm

import os
from selenium.webdriver.common.by import By
from aicc_Cloud.aicc_Project.aicc_Page.ruisi_Page import Page

class whrw_page(Page):
    '''
     ================================定义基本元素,元祖=================================
    '''
    #定义进入外呼任务页面 元素
    task = (By.XPATH,"//*[@id='views']/aside/ul/li[3]/span[2]")
    #定义导出明细按钮 元素
    task_dcmx = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/div/button[2]/span")
    #定义查看详情按钮 元素
    task_ckxq = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/div/button[1]/span")
    #定义查看详情-查看详情按钮 元素
    task_ckxq_ckxq = (By.XPATH,"//*[@id='scroll']/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[10]/div/div/button[1]/span")
    #定义查看详情-查看详情-播放录音按钮 元素
    task_ckxq_ckxq_bfly = (By.XPATH,"//*[@id='scroll']/div/div[4]/div/div[2]/div/div[1]/div/div[2]/button[2]/span/i")
    # #定义查看详情-查看详情-关闭 元素
    # task_ckxq_ckxq_gb = (By.XPATH,"//*[@class='el-icon-close']")
    #定义查看详情-导出录音按钮 元素
    task_ckxq_dcly = (By.XPATH,"//*[@id='scroll']/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[10]/div/div/button[2]/span")
    #定义批量导出明细 元素
    task_pldc_mx = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span")
    #定义批量导出-点击选中导出 元素
    task_pldc_mx_xzdc = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div/form/div[6]/div/button[3]/span")
    #定义 外呼任务(任务状态)元素
    task_whrw_rwzt = (By.XPATH,"//*[@autocomplete='off']")
    #定义 外呼任务(选择任务)元素
    task_whrw_rwzt_xz = (By.XPATH,"//*[@x-placement='bottom-start']/div/div/ul/li[2]")
    #定义 重置按钮 元素
    task_cz = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div/form/div[6]/div/button[2]/span")
    #定义 查询 元素
    task_cx = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div/form/div[6]/div/button[1]/span")
    '''
     ================================定义基本元素,元祖 方法=================================
    '''
    def task_log(self):
        #定义进入外呼任务页面 元素方法
        return self.find_element(*self.task).click()

    def task_dcmx_log(self):
        #定义导出明细按钮 元素方法
        self.find_element(*self.task_dcmx).click()
        os.system("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_BatchUpload\\dcmx.exe")

    def task_ckxq_log(self):
        #定义查看详情按钮 元素方法
        return self.find_element(*self.task_ckxq).click()

    def task_ckxq_ckxq_log(self):
        #定义查看详情-查看详情按钮 元素方法
        return self.find_element(*self.task_ckxq_ckxq).click()

    def task_ckxq_ckxq_bfly_log(self):
        #定义查看详情-查看详情-播放录音按钮 元素方法
        return self.find_element(*self.task_ckxq_ckxq_bfly).click()


    def task_ckxq_ckxq_gb_log(self):
        #定义查看详情-查看详情-关闭 元素方法
        return self.driver.back()
        #self.find_element(*self.task_ckxq_ckxq_gb).click()
        # self.find_element(*self.task_ckxq_ckxq_gb).back()

    def task_ckxq_dcly_log(self):
        #定义查看详情-导出录音按钮 元素方法
        return self.find_element(*self.task_ckxq_dcly).click()
        os.system("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_BatchUpload\\Dcly.exe")

    def task_pldc_mx_log(self):
        #定义批量导出明细 元素方法
        self.find_element(*self.task_pldc_mx).click()

    def task_pldc_mx_xzdc_log(self):
        #定义批量导出-点击选中导出 元素方法
        self.find_element(*self.task_pldc_mx_xzdc).click()
        os.system("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_BatchUpload\\xzdc.exe")

    def task_whrw_rwzt_log(self):
        #定义 外呼任务(任务状态) 元素方法
        return self.find_element(*self.task_whrw_rwzt).click()

    def task_whrw_rwzt_xz_log(self):
        #定义 外呼任务(选择任务)元素方法
        return self.find_element(*self.task_whrw_rwzt_xz).click

    def task_cz_log(self):
        #定义 重置按钮 元素方法
        return self.find_element(*self.task_cz).click()

    def task_cx_log(self):
        #定义 查询 元素方法
        return self.find_element(*self.task_cx).click()

    '''
    ================================断言验证 元素=================================
    '''
    task_assert = (By.XPATH,"//*[@id='views']/aside/ul/li[3]/span[2]")


    '''
    ================================断言验证 元素方法=================================
    '''
    def task_assert_log(self):
        return self.find_element(*self.task_assert).text