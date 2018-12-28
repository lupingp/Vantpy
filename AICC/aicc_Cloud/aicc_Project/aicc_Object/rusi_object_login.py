# -*- coding: utf-8 -*-
# @Time    : 2018/11/5  18:51
# @Author  : 陆平！！
# @FileName: rusi_Lj.py
# @Software: PyCharm

from selenium.webdriver.common.by import By
from AICC.aicc_Cloud.aicc_common.ruisi_Base import BasePage
import time

class Login_Page(BasePage):
    '''''登录页面模型'''
    # url = ""
    #定位器，定位需要用到的元素，元组

    username_loc = (By.XPATH,"//*[@id='views']/div[2]/div/form/div[1]/div/div/input")

    password_loc =(By.XPATH,"//*[@id='views']/div[2]/div/form/div[2]/div/div/input")

    submit_loc =(By.XPATH,"//*[@id='views']/div[2]/div/form/div[4]/div/button")
    # 打开退出元素
    tuichu_denglu = (By.CLASS_NAME, 'el-dropdown-selfdefine')
    # 点击退出登陆元素
    quit_log = (By.XPATH, "/html/body/ul/li[2]")
    # 点击确定,退出成功
    quit_queding = (By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span")
    # 登录成功后获取Welcome
    welcome_1 = ("xpath", "//*[@id='scroll']/div/div/h1")
    # 登录成功后获取主页面（睿思智能客服平台）
    welcome = ("xpath", "//*[@id='scroll']/div/div/p")

    #action，把每个操作封装为一个方法
    #账号输入框的操作方法
    def type_username(self,text):
        self.send_key(self.username_loc,text)
        # return self.find_element(*self.username_loc).send_keys(username)
    #密码输入框的操作方法
    def type_password(self,password):
        self.send_key(self.password_loc,password)
        # return self.find_element(*self.password_loc).send_keys(password)
    #提交按钮操作方法
    def type_submit(self):
        self.click(self.submit_loc)
        # return self.find_element(*self.submit_loc).click()

    def tuichu(self):
        # 登陆成功后打开退出登陆
        return self.click(self.tuichu_denglu)

    def quitloc(self):
        # 点击退出登陆
        return self.click(self.quit_log)

    def quitqueding(self):
        # 点击确定 退出成功
        return self.click(self.quit_queding)

    #写一个同一登录的入口，其他用例也会调用该登录方法
    def user_login(self,username='',password=''):
        self.type_username(username)
        self.type_password(password)
        self.type_submit()
        #判断登录是否成功,如果成功 就判断首页是否存在Welcome 然后在判断是否存在 睿思智能客服云平台
        # result_1 = self.get_text(self.welcome_1)
        # if result_1 == "Welcome":
        #     result = self.get_text(self.welcome)
        #     if result == "睿思智能客服云平台":
        #         zen.click(self.tuichu_denglu)
        #         zen.click(self.quit_log)
        #         zen.click(self.quit_queding)
        #     else:
        #         print("获取睿思智能客服云平台失败")
        # else:
        #     print("获取Welcome失败")

    # 写一个同一退出的入口，其他用例也会调用该登录方法
    def user_tuichu(self):
        self.tuichu()
        self.quitloc()
        time.sleep(0.8)
        self.quitqueding()

    # 定位器：错误提示
    #用户名为空
    username_error = (By.XPATH,"//*[@id='views']/div[2]/div/form/div[1]/div/div[2]")
    #密码为空
    password_error = (By.XPATH,"//*[@id='views']/div[2]/div/form/div[2]/div/div[2]")
    #错误登陆提示语
    denglu_tishi_error = (By.XPATH,"/html/body/div[2]")
    #错误用户名错误
    user_name_error = (By.CLASS_NAME,"el-message__content")

    # 用户名为空
    def type_username_error(self):
        return self.get_text(self.username_error)

    # 密码为空
    def type_password_error(self):
        return self.get_text(self.password_error)

    # 错误登陆提示语
    def type_denglu_tishi_error(self):
        return self.get_text(self.denglu_tishi_error)

    # 用户名不存在错误
    def type_user_name_error(self):
        return self.get_text(self.user_name_error)

    #登陆成功
    def type_denglu_success(self):
        return self.get_text(self.welcome_1)