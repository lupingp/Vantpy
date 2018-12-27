# -*- coding: utf-8 -*-
# @Time    : 2018/11/8  18:58
# @Author  : 陆平！！
# @FileName: ruisi_jqrsc_case_2.py
# @Software: PyCharm

import time
import datetime
import unittest
from AICC.aicc_Cloud.aicc_Plu.aicc_plu_screenshots.screenshots_jqrsc import jqrsc_screenshots
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_login import Login_Page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.ruisi_object_jqrsc import jqrsc_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_xtjk import xtjk_page


class Test_jqrsc_model(jqrsc_screenshots,Login_Page,jqrsc_page,xtjk_page):
    '''机器人市场模块'''

    def user_login_verify(self,username="",password=""):
        self.login_page.user_login(username,password)

    def test_1(self):
        '''测试用例1：访问机器人市场'''
        self.user_login_verify(username="test0012",password="111111")
        time.sleep(2)
        self.jqrsc()
        time.sleep(2)
        self.jqrsc_jietu_case_1()
        time.sleep(1)
        try:
            self.assertEqual(self.type_jqrsc_page_error(),u"机器人市场")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" %msg)
        else:
            print("验证成功!")
        self.login_page.tuichu()
        time.sleep(1)
        self.login_page.quitloc()
        time.sleep(2)
        self.login_page.quitqueding()
        time.sleep(2)

    def test_2(self):
        '''测试用例2：复制我的机器人-机器人名字-机器人介绍-复制成功'''
        self.user_login_verify(username="test0012",password="111111")
        time.sleep(1)
        self.jqrsc()
        time.sleep(2)
        self.fuzhi_wdjqr()
        time.sleep(1)
        self.jqrsc_jietu_case_2()
        time.sleep(1)
        self.jqrsc_name_loc()
        try:
            now_time = datetime.datetime.now()
            s_time = ("我的秒数是%s" %now_time.second)
            ss_time = ("大家好，我的秒数是%s初次和大家见面请多多关照！！" %now_time.second)
            self.assertIn(self.type_jqrsc_name_error(),s_time,msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" %msg)
        else:
            print("验证成功!")
        self.jqrsc_troduce_loc()
        try:
            self.assertIn(self.type_jqrsc_introduce_error(),ss_time,msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print("%r" %msg)
        else:
            print("验证成功!")
        time.sleep(2)
        self.jqrsc_determine_loc()
        time.sleep(0.5)
        self.jqrsc_jietu_case_2_1()
        time.sleep(0.5)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(1)
        self.quitqueding()
        time.sleep(2)

    def test_3(self):
        '''测试用例3：复制我的机器人-机器人名字-机器人介绍-重名验证'''
        self.user_login_verify(username="test0012",password="111111")
        time.sleep(1)
        self.jqrsc()
        time.sleep(2)
        self.fuzhi_wdjqr()
        time.sleep(1)
        self.jqrsc_determine_loc()
        try:
            self.assertEqual(self.type_jqrsc_cm_error(),"机器人名重复！")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" %msg)
        else:
            print("验证成功!")
        time.sleep(2)
        self.jqrsc_determine_loc()
        self.jqrsc_jietu_case_3()
        time.sleep(1)
        self.jiqiren_quxiao_loc()
        time.sleep(0.5)
        self.login_page.tuichu()
        time.sleep(1)
        self.login_page.quitloc()
        time.sleep(1)
        self.login_page.quitqueding()
        time.sleep(2)

    def test_4(self):
        """测试用例4：电话体检-输入电话号码-输入任务名(数字)-点击发送外呼"""
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.jqrsc()
        time.sleep(1)
        self.phone_number_log()
        time.sleep(1)
        self.shuru_phone_log()
        try:
            self.assertIn(self.type_jqrsc_phone_error(), "18811730879", msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        self.jqrsc_rw_log()
        try:
            self.assertIn(self.type_jqrsc_rw_error(), "123456789", msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print("%r" % msg)
        else:
            print("验证成功!")
        self.waihu_log()
        time.sleep(1)
        if u'限30个字，必须包含中文或英文，支持阿拉伯数字、英文下划线' == self.type_jqrsc_rw_name_error():
            print("通过")
        else:
            print("失败")
        self.jqrsc_jietu_case_4()
        time.sleep(1)
        self.waihu_quxiao_loc()
        time.sleep(0.5)
        self.login_page.tuichu()
        time.sleep(1)
        self.login_page.quitloc()
        time.sleep(1)
        self.login_page.quitqueding()
        time.sleep(2)


    def test_5(self):
        """测试用例5：电话体检-输入电话号码(>11位,<11位)-输入任务名(数字)-点击发送外呼"""
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.jqrsc()
        time.sleep(2)
        self.phone_number_log()
        time.sleep(1)
        self.shuru_phone_log_1()
        try:
            self.assertIn(self.type_jqrsc_phone_error(), "18811730879", msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        self.jqrsc_rw_log_1()
        try:
            self.assertIn(self.type_jqrsc_rw_error(), "陆平", msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print("%r" % msg)
        else:
            print("验证成功!")
        self.waihu_log()
        try:
            self.assertEqual(self.type_jqrsc_shuru_phone_log_error(), "手机号输入内容不合法")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        time.sleep(0.5)
        self.jqrsc_jietu_case_5()
        time.sleep(1)
        self.waihu_quxiao_loc()
        time.sleep(0.5)
        self.login_page.tuichu()
        time.sleep(1)
        self.login_page.quitloc()
        time.sleep(1)
        self.login_page.quitqueding()
        time.sleep(2)

    def test_6(self):
        """测试用例6：不输入手机号,任务名 点击发起外呼"""
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.jqrsc()
        time.sleep(2)
        self.phone_number_log()
        time.sleep(1)
        self.waihu_log()
        time.sleep(1)
        self.jqrsc_jietu_case_6()
        try:
            self.assertEqual(self.type_jqrsc_null_error(),"手机号不能为空",msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        self.waihu_quxiao_loc()
        time.sleep(1)
        self.login_page.tuichu()
        time.sleep(1)
        self.login_page.quitloc()
        time.sleep(1)
        self.login_page.quitqueding()
        time.sleep(2)

    def test_7(self):
        """测试用例7：输入正确的手机号,任务名 点击发起外呼-发送成功"""
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.jqrsc()
        time.sleep(2)
        self.phone_number_log()
        time.sleep(1)
        self.shuru_phone_log()
        try:
            self.assertIn(self.type_jqrsc_phone_error(), "18811730879", msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        self.jqrsc_rw_log_1()
        try:
            self.assertIn(self.type_jqrsc_rw_error(), "陆平", msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print("%r" % msg)
        else:
            print("验证成功!")
        self.waihu_log()
        time.sleep(1)
        self.jqrsc_jietu_case_7_1()
        try:
            self.assertIn(self.type_jqrsc_waihu_log_error(), "任务创建成功!")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        time.sleep(1)
        self.xitong_jiankong_log()
        time.sleep(0.5)
        self.jqrsc_jietu_case_7_2()
        time.sleep(13)
        self.login_page.tuichu()
        time.sleep(1)
        self.login_page.quitloc()
        time.sleep(1)
        self.login_page.quitqueding()
        time.sleep(2)


