# -*- coding: utf-8 -*-
# @Time    : 2018/11/8  22:59
# @Author  : 陆平！！
# @FileName: ruisi_object_jqrsc.py
# @Software: PyCharm

import time
import datetime
from selenium.webdriver.common.by import By
from aicc_Cloud.aicc_Project.aicc_Page.ruisi_Page import Page

class jqrsc_page(Page):
    #===========================================机器人管理页面==================================================
    '''机器人管理页面'''
    # url = ""
    # 定位器，定位需要用到的元素，元组
    # 点击机器人市场元素
    '''
            【机器人】-测试专业机器人导出流程
    '''
    jqr_maiker = (By.XPATH, "//*[@id='views']/aside/ul/li[1]/span[2]")
    # 点击复制我的机器人
    fuzhi_jqr = (By.XPATH, "//*[@id='scroll']/div/div/div[1]/div[3]/div[1]/div/div[7]/button[2]/span")
    # 输入机器人名称
    jiqiren_name = (By.XPATH, "//*[@id='scroll']/div/div/div[2]/div/div[2]/form/div[2]/div/div/input")
    # 输入机器人介绍
    jiqiren_jieshao = (By.XPATH, '//*[@id="scroll"]/div/div/div[2]/div/div[2]/form/div[3]/div/div/textarea')
    # 点击确定,
    jiqiren_determine = (By.XPATH, '//*[@id="scroll"]/div/div/div[2]/div/div[2]/form/div[4]/div/button[1]/span')
    # 点击取消
    jqr_quxiao = (By.XPATH, "//*[@id='scroll']/div/div/div[2]/div/div[2]/form/div[4]/div/button[2]/span")
    # 只输入用户名点击登陆
    denglu_error = (By.CLASS_NAME, 'el-form-item__error')
    # 点击电话体验
    phone_number = (By.XPATH, '//*[@id="scroll"]/div/div/div[1]/div[3]/div[1]/div/div[7]/button[1]/span')
    # 输入电话号码
    shuru_phone = (By.XPATH, '//*[@id="scroll"]/div/div/div[3]/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[1]/div[2]/div/input')
    # 输入任务名称
    jqrsc_rw = (By.XPATH, "//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[2]/div/div/input")
    # #选择主叫号码
    # shuru_number = (By.XPATH,"//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[3]/div/div/div/input")
    # # 选择号码028
    # shuru_number_zero = (By.XPATH,"/html/body/div[14]/div[1]/div[1]/ul/li/span")
    # #展开高级设置
    # zhankai_shezhi = (By.CLASS_NAME,'el-icon-arrow-down')
    # # 设置等待时常
    # shezhi_time = (By.XPATH,"//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[4]/div[2]/div/div/input")
    # 点击发起外呼
    waihu = (By.XPATH, "//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[6]/div/button[1]")
    # 点击取消
    waihu_quxiao = (By.XPATH,"//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[6]/div/button[2]")
 #=================================================定义元素方法================================================
    def jqrsc(self):
        #点击机器人市场
        self.find_element(*self.jqr_maiker).click()

    def fuzhi_wdjqr(self):
        #点击复制我的机器人
        self.find_element(*self.fuzhi_jqr).click()

    def jqrsc_name_loc(self):
        #输入机器人名称
        self.find_element(*self.jiqiren_name).clear()
        now_time = datetime.datetime.now()
        s_time = ("我的秒数是%s" %now_time.second)
        self.find_element(*self.jiqiren_name).send_keys(s_time)

    def jqrsc_troduce_loc(self):
        # 输入机器人介绍
        self.find_element(*self.jiqiren_jieshao).clear()
        now_time = datetime.datetime.now()
        s_time = ("大家好，我的秒数是%s初次和大家见面请多多关照！！" %now_time.second)
        self.find_element(*self.jiqiren_jieshao).send_keys(s_time)

    def jqrsc_determine_loc(self):
        #点击确定
        self.find_element(*self.jiqiren_determine).click()

    def jiqiren_quxiao_loc(self):
        # 点击取消按钮
        self.find_element(*self.jqr_quxiao).click()

    def phone_number_log(self):
        #点击电话体检
        self.find_element(*self.phone_number).click()

    def shuru_phone_log(self):
        #输入手机号
        self.find_element(*self.shuru_phone).clear()
        # now_time = datetime.datetime.now()
        # s_time = ("当前秒是%s"%now_time.second)
        self.find_element(*self.shuru_phone).send_keys("18811730879")

    def shuru_phone_log_1(self):
        #输入手机号
        self.find_element(*self.shuru_phone).clear()
        now_time = datetime.datetime.now()
        s_time = ("%s"%now_time.second)
        self.find_element(*self.shuru_phone).send_keys(s_time)

    def jqrsc_rw_log(self):
        #输入 测试专业机器人导出流程机器人的 参数:任务名称
        self.find_element(*self.jqrsc_rw).clear()
        now_time = datetime.datetime.now()
        s_time = ("%s"%now_time.second)
        self.find_element(*self.jqrsc_rw).send_keys(s_time)

    def jqrsc_rw_log_1(self):
        #输入 测试专业机器人导出流程机器人的 参数:任务名称
        self.find_element(*self.jqrsc_rw).clear()
        now_time = datetime.datetime.now()
        s_time = ("当前秒是%s"%now_time.second)
        self.find_element(*self.jqrsc_rw).send_keys(s_time)
    # def shuru_number_loc(self):
    #     # 定义选择号码
    #     self.find_element(*self.shuru_number).click()
    #
    # def shuru_number_zero_loc(self):
    #     #定义号码
    #     self.find_element(*self.shuru_number_zero).click()
    #
    # def zhankai_shezhi_loc(self):
    #     # 定义打开高级设置
    #     self.find_element(*self.zhankai_shezhi).click()
    #
    # def shezhi_time_loc(self):
    #     #设置等待时常
    #     self.find_element(*self.shezhi_time).clear()
    #     self.find_element(*self.shezhi_time).send_keys('20')

    def waihu_log(self):
        #点击发起外呼
        self.find_element(*self.waihu).click()

    def waihu_quxiao_loc(self):
        #外呼取消方法
        self.find_element(*self.waihu_quxiao).click()

    # ==========================================定位器：错误提示===========================================
    #错误的机器人名字 断言验证
    jqrsc_name_error = (By.XPATH,"//*[@id='scroll']/div/div/div[2]/div/div[2]/form/div[4]/div/button[1]")
    #输入错误的任务名称点击发起外呼 断言验证
    jqrsc_rw_name_error = (By.XPATH,"//*[@id='scroll']/div/div/div[3]/div/div[2]/div[1]/form/div[2]/div/div[2]")
    #输入错误的手机号点击发起外呼 断言验证
    jqrsc_shuru_phone_log_error = (By.XPATH,"/html/body/div[14]")
    #不输入手机号、任务名称、点击发起外呼 断言验证
    jqrsc_null_error = (By.CLASS_NAME,"el-message__content")
    #发送外呼成功后 断言验证
    jqrsc_waihu_log_error = (By.CLASS_NAME,"el-message__content")
    #验证进入机器人市场
    def type_jqrsc_page_error(self):
        return self.find_element(*self.jqr_maiker).text

    #验证复制我的输入机器人名称、介绍文本
    def type_jqrsc_name_error(self):
        return self.find_element(*self.jiqiren_name).text

    def type_jqrsc_introduce_error(self):
        return self.find_element(*self.jiqiren_jieshao).text

    #验证重新 打印机器人名字重复
    def type_jqrsc_cm_error(self):
        return self.find_element(*self.jqrsc_name_error).text

    #验证 测试专业机器人导出流程机器人的 参数:手机号
    def type_jqrsc_phone_error(self):
        return self.find_element(*self.shuru_phone).text

    #验证 测试专业机器人导出流程机器人的 参数:任务名称
    def type_jqrsc_rw_error(self):
        return self.find_element(*self.jqrsc_rw).text

    #验证 测试专业机器人导出流程机器人的 输入数字的任务名称点击发起外呼
    def type_jqrsc_rw_name_error(self):
        return  self.find_element(*self.jqrsc_rw_name_error).text

    #验证 测试专业机器人导出流程机器人的 输入错误的手机号点击发起外呼
    def type_jqrsc_shuru_phone_log_error(self):
        return self.find_element(*self.jqrsc_shuru_phone_log_error).text

    #验证 不输入手机号、任务名称、点击发起外呼
    def type_jqrsc_null_error(self):
        return self.find_element(*self.jqrsc_null_error).text

    #验证 测试专业机器人导出流程机器人的 输入正确的任务名称、手机号点击发起外呼
    def type_jqrsc_waihu_log_error(self):
        return self.find_element(*self.jqrsc_waihu_log_error).text




