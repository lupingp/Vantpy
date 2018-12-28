# -*- coding: utf-8 -*-
# @Time    : 2018/11/5  18:52
# @Author  : 陆平！！
# @FileName: ruisi_login_case_1.py
# @Software: PyCharm

from aicc_Cloud.aicc_Log.logger import Logger
from aicc_Cloud.aicc_Plu.ruisi_public import MyTest
from aicc_Cloud.aicc_Project.aicc_Object.rusi_object_login import Login_Page
from aicc_Cloud.aicc_common.ruisi_Base import BasePage

logger = Logger(logger="test_1_login_case").getlog()
class Test_login_model(MyTest,Logger,BasePage):
    '''登陆模块：测试用例'''
    def test_1(self):
        '''测试用例1：用户名空，密码正确'''
        One = Login_Page(self.driver)
        One.user_login(username='',password='111111')
        try:
            self.assertEqual(One.type_username_error(),"请输入用户名")
        except BaseException as msg:
            logger.info("Login_Test_1_用户名下拉失败:%r" %msg)
            One.get_screent_img('验证用户名下拉失败')
        else:
            logger.info("验证用户名下拉成功！")
            One.get_screent_img('Login_Test_1_1_验证用户名下拉成功')
        One.F5()

    def test_2(self):
        '''''测试用例2：用户名正确，密码为空'''
        One = Login_Page(self.driver)
        One.user_login(username='test0012',password='')
        try:
            self.assertEqual(One.type_password_error(),"请输入密码")
        except BaseException as msg:
            logger.info("验证密码下拉提示失败：%r "%msg)
            One.get_screent_img('Login_Test_2_验证密码下拉提示失败')
        else:
            logger.info("验证密码下拉提示成功！")
            One.get_screent_img('Login_Test_2_1_验证密码下拉提示成功')
        One.F5()

    def test_3(self):
        '''测试用例3：用户名 密码都为空'''
        One = Login_Page(self.driver)
        One.user_login(username='',password='')
        try:
            self.assertEqual(One.type_username_error(), "请输入用户名")
            self.assertEqual(One.type_password_error(), "请输入密码")
        except BaseException as msg:
            logger.info("验证用户名/密码下拉提示失败:%r" %msg)
            One.get_screent_img('Login_Test_3_验证用户名,密码下拉提示失败')
        else:
            logger.info("验证用户名/密码下拉提示成功！")
            One.get_screent_img('Login_Test_3_1_验证用户名,密码下拉提示成功')
        One.F5()

    def test_4(self):
        '''''测试用例4：用户名为特殊字符(*- $%^&./';l)+数字 密码正确'''
        One = Login_Page(self.driver)
        One.user_login(username="*&@./789789",password="111111")
        try:
            self.assertEqual(One.type_denglu_tishi_error(),"用户名不存在")
        except BaseException as msg:
            logger.info("验证用户名提示失败：%r" %msg)
            One.get_screent_img('Login_Test_4_验证用户名提示失败')
        else:
            logger.info("验证用户名提示成功")
            One.get_screent_img('Login_Test_4_1_验证用户名提示成功')
        One.F5()

    def test_5(self):
        '''测试用例5：用户名正确 密码为特殊字符(*- $%^&./';l)+数字'''
        One = Login_Page(self.driver)
        One.user_login(username="test0012",password="*&@./789789")
        try:
            self.assertEqual(One.type_denglu_tishi_error(),"用户密码错误，请重试！")
        except BaseException as msg:
            logger.info("验证密码提示失败：%r" %msg)
            One.get_screent_img('Login_Test_5_验证密码提示失败')
        else:
            logger.info("验证密码提示成功")
            One.get_screent_img('Login_Test_5_1_验证密码提示成功')
        One.F5()

    def test_6(self):
        '''测试用例6：用户名输入超长(数字+字母) 密码为特殊字符(*- $%^&./';l)+数字'''
        One = Login_Page(self.driver)
        One.user_login(username="78998898444444444EEEEEEEEEEEEvv",password="*- $%^&./';l")
        try:
            self.assertEqual(One.type_user_name_error(), "用户名不存在")
        except BaseException as msg:
            logger.info("验证失败:%r" %msg)
            One.get_screent_img('Login_Test_6_验证失败')
        else:
            logger.info("断言成功")
            One.get_screent_img('Login_Test_6_1_验证失败')
        One.F5()

    def test_7(self):
        '''测试用例7：用户名输入特殊字符(*- $%^&./';l)+数字 密码为超长(数字+字母)'''
        One = Login_Page(self.driver)
        One.user_login(username="*- $%^&./';l",password="78998898444444444EEEEEEEEEEEEvv")
        try:
            self.assertEqual(One.type_user_name_error(), "用户名不存在")
        except BaseException as msg:
            logger.info("验证失败:%r" %msg)
            One.get_screent_img('Login_Test_7_验证失败')
        else:
            logger.info("验证成功")
            One.get_screent_img('Login_Test_7_1_验证失败')
        One.F5()

    def test_8(self):
        '''测试用例8：用户名正确 密码正确'''
        One = Login_Page(self.driver)
        One.user_login(username="test0012",password="111111")
        try:
            self.assertEqual(One.type_denglu_success(),"Welcome")
        except BaseException as msg:
            logger.info("验证登录失败:%r" %msg)
            One.get_screent_img('Login_Test_8_验证登录失败')
        else:
            logger.info("验证登录成功")
            One.get_screent_img('Login_Test_8_1_验证登录成功')
        One.tuichu()
        One.quitloc()
        One.quitqueding()