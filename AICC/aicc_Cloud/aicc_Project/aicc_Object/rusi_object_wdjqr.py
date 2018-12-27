# -*- coding: utf-8 -*-
# @Time    : 2018/11/13  11:27
# @Author  : 陆平！！
# @FileName: rusi_object_wdjqr.py
# @Software: PyCharm

import time
import os
import datetime
from selenium.webdriver.common.by import By
from aicc_Cloud.aicc_Project.aicc_Page.ruisi_Page import Page

class wdjqr_page(Page):
    '''
     ================================定义基本元素,元祖=================================
    '''
    #定义我的机器人 元素
    wdjqr_robot = (By.CLASS_NAME,"robot")
    #定义机器人姓名 元素
    wdjqr_name = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/div/p[1]/span")
    #定义复制复制机器人ID 元素
    wdjqr_ID = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/div/p[2]/i[1]")
    #定义批量发起外呼 元素
    wdjqr_pl_wh = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button[2]/span")
    #定义批量发起外呼-选取文件 元素
    wdjqr_pl_wh_xqwj = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[1]/div/div/div/div/div[1]/button")
    #定义批量发起外呼-选取文件-输入任务名 元素
    wdjqr_pl_wh_xqwj_rwm = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[2]/div/div/input")
    #定义批量发起外呼-选取文件-输入任务名-发起外呼 元素
    wdjqr_pl_wh_xqwj_rwm_fqwh = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[6]/div/button[1]/span")
    #定义 正常外呼 元素
    wdjqr_zcwh = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[2]/div[2]/button[1]/span")
    #定义 正常外呼-输入手机号 元素
    wdjqr_phone = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[1]/div/div[2]/div/div[1]/div[2]/div/input")
    #定义 正常外呼-任务名称 元素
    wdjqr_rw_name = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[2]/div/div/input")
    #定义 正常外呼-发起外呼 元素
    wdjqr_fqwh = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[2]/div/div[2]/div[3]/form/div[6]/div/button[1]/span")
    #定义 查看参数 元素
    wdjqr_ckcs = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/button[4]")
    #定义 查看参数-关闭查看参数
    # wdjqr_ckcs_gb = (By.XPATH,"/html/body/div[3]/div/div[1]/button/i")
    #定义 查看短信 元素
    wdjqr_ckdx = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/button[5]/i")
    #定义 复制新版本 元素
    wdjqr_fzbb = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/div[1]/div[2]/button[1]")
    #定义 复制新版本-确定 元素
    wdjqr_fzbb_qd = (By.CSS_SELECTOR,"body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--small.el-button--primary > span")

    '''
     ================================定义基本元素,元祖 方法=================================
    '''
    def wdjqr_robot_log(self):
        # 定义我的机器人元素方法
        return self.find_element(*self.wdjqr_robot).click()

    def wdjqr_name_log(self):
        # 定义机器人姓名元素方法
        return self.find_element(*self.wdjqr_name).text

    def wdjqr_ID_log(self):
        # 定义复制复制机器人ID元素方法
        return self.find_element(*self.wdjqr_ID).click()

    def wdjqr_pl_wh_log(self):
        # 定义批量发起外呼元素方法
        return self.find_element(*self.wdjqr_pl_wh).click()

    def wdjqr_pl_wd_xqwj_log(self):
        # 定义批量发起外呼-选取文件元素方法
        self.find_element(*self.wdjqr_pl_wh_xqwj).click()
        os.system("E:\\SoftwareTesting\\Projectpath\\AICC\\aicc_Cloud\\aicc_BatchUpload\\Plsc.exe")

    def wdjqr_pl_wh_xqwj_rwm_log(self):
        #定义批量发起外呼-选取文件-输入任务名元素方法
        now_time = datetime.datetime.now()
        s_time = ("当前秒是%s" %now_time.second)
        return self.find_element(*self.wdjqr_pl_wh_xqwj_rwm).send_keys(s_time)

    def wdjqr_pl_wh_xqwj_rwm_fqwh_log(self):
        #定义批量发起外呼-选取文件-输入任务名-发起外呼 元素方法
        return self.find_element(*self.wdjqr_pl_wh_xqwj_rwm_fqwh).click()

    def wdjqr_zhwh_log(self):
        #定义正常外呼 元素方法
        return self.find_element(*self.wdjqr_zcwh).click()

    def wdjqr_phone_log(self):
        #定义 正常外呼-输入手机号 元素方法
        return self.find_element(*self.wdjqr_phone).send_keys("18811730879")

    def wdjqr_rw_name_log(self):
        #定义 正常外呼-任务名称 元素方法
        now_time = datetime.datetime.now()
        s_time = ("当前秒是%s" % now_time.second)
        return self.find_element(*self.wdjqr_rw_name).send_keys(s_time)

    def wdjqr_fqwh_log(self):
        #正常外呼-发起外呼 元素方法
        return self.find_element(*self.wdjqr_fqwh).click()

    def wdjqr_ckcs_log(self):
        #定义 查看参数 元素方法
        return self.find_element(*self.wdjqr_ckcs).click()

    def wdjqr_ckcs_gb_log(self):
        #定义 查看参数-关闭查看参数 元素方法
        return self.driver.back()

    def wdjqr_ckdx_log(self):
        #定义 查看短信 元素方法
        return self.find_element(*self.wdjqr_ckdx).click()

    def wdjqr_fzbb_log(self):
        #定义 复制版本 元素方法
       return self.find_element(*self.wdjqr_fzbb).click()

    def wdjqr_fzbb_qd_log(self):
        #复制新版本-确定 元素方法
        return self.find_element(*self.wdjqr_fzbb_qd).click()

    '''
    ================================定义错误元素,元祖=================================
    '''
    #定义进入机器人页面title 元素
    wdjqr_title = (By.XPATH,"//*[@id='scroll']/div/div[2]/div[1]/div[1]/div/span")
    #定义复制复制机器人ID返回元素
    wdjqr_ID_return = (By.CLASS_NAME,"el-message__content")
    #定义 判断查看短信 文本 元素
    wdjqr_ckdx_title = (By.XPATH,"//*[@id='scroll']/div/div/div[1]/div/span")
    #定义 复制版成功后的 元素
    wdjqr_fzbb_asser = (By.CLASS_NAME,"el-message__content")
    '''
    ================================定义错误元素,元祖 方法=================================
    '''
    def type_wdjqr_title(self):
        #定义进入机器人页面title 元素方法
        return self.find_element(*self.wdjqr_title).text

    def type_wdjqr_ID_return(self):
        #定义复制复制机器人ID返回元素方法
        return self.find_element(*self.wdjqr_ID_return).text

    def type_wdjqr_ckdx_title(self):
        #定义 判断查看短信 文本 元素方法
        return self.find_element(*self.wdjqr_ckdx_title).text

    def type_wdjqr_fzbb_asser(self):
        #定义 复制版成功后的 元素方法
        self.find_element(*self.wdjqr_fzbb_asser).text
        self.driver.refresh()