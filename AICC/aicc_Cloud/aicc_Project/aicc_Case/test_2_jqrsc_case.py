# -*- coding: utf-8 -*-
# @Time    : 2018/11/8  18:58
# @Author  : 陆平！！
# @FileName: ruisi_jqrsc_case_2.py
# @Software: PyCharm

import time
import datetime
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_login import Login_Page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.ruisi_object_jqrsc import jqrsc_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_xtjk import xtjk_page
from AICC.aicc_Cloud.aicc_common.ruisi_Base import BasePage
from AICC.aicc_Cloud.aicc_Log.logger import Logger
from AICC.aicc_Cloud.aicc_Plu.ruisi_public import MyTest
import random

logger = Logger(logger="test_2_jqrsc_case").getlog()
class Test_jqrsc_model(MyTest,Login_Page,jqrsc_page,xtjk_page,BasePage):

    '''机器人市场模块'''
    # def test_1(self):
    #     '''测试用例1：访问机器人市场'''
    #     One = jqrsc_page(self.driver)
    #     Two = Login_Page(self.driver)
    #     Two.user_login(username="test0012",password="111111")
    #     One.jqrsc()
    #     One.get_screent_img("Test_jqrsc_1_访问机器人市场")
    #     try:
    #         self.assertEqual(self.type_jqrsc_page_error(),u"机器人市场")
    #     except BaseException as msg:
    #         logger.info("访问机器人市场验证失败!%r" %msg)
    #     else:
    #         logger.info("访问机器人市场验证成功!")
    #     Two.user_tuichu()
    #
    # def test_2(self):
    #     '''测试用例2：复制我的机器人-机器人名字-机器人介绍-复制成功'''
    #     One = jqrsc_page(self.driver)
    #     Two = Login_Page(self.driver)
    #     Two.user_login(username="test0012",password="111111")
    #     One.jqrsc()
    #     One.fuzhi_wdjqr()
    #     One.get_screent_img("Test_jqrsc_2_显示复制我的机器人弹窗")
    #     now_time = int(time.time())
    #     s_time = ("我的秒数是%s" %now_time)
    #     One.jqrsc_name_loc(s_time)
    #     try:
    #         # now_time = datetime.datetime.now()
    #         # s_time = ("我的秒数是%s" %now_time.second)
    #         # ss_time = ("大家好，我的秒数是%s初次和大家见面请多多关照！！" %now_time.second)
    #         self.assertIn(self.type_jqrsc_name_error(),s_time,msg="失败")
    #     except BaseException as msg:
    #         logger.info("验证机器人名字失败：%r" %msg)
    #     else:
    #         logger.info("验证机器人名字成功!")
    #     now_time = datetime.datetime.now()
    #     ss_time = ("大家好，我的秒数是%s初次和大家见面请多多关照！！" % now_time.second)
    #     self.jqrsc_troduce_loc(ss_time)
    #     try:
    #         self.assertIn(self.type_jqrsc_introduce_error(),ss_time,msg="失败")
    #     except BaseException as msg:
    #         logger.info("验证失败:%r" %msg)
    #     else:
    #         logger.info("验证成功!")
    #     One.jqrsc_determine_loc()
    #     One.get_screent_img("Test_jqrsc_2_1_复制机器人成功")
    #     Two.user_tuichu()

    # def test_3(self):
    #     '''测试用例3：复制我的机器人-机器人名字-机器人介绍-重名验证'''
    #     One = jqrsc_page(self.driver)
    #     Two = Login_Page(self.driver)
    #     Two.user_login(username="test0012",password="111111")
    #     One.jqrsc()
    #     One.fuzhi_wdjqr()
    #     try:
    #         self.assertIn(self.type_jqrsc_cm_error(),"机器人名重复！")
    #     except BaseException as msg:
    #         logger.info("复制机器人重名验证失败：%r" %msg)
    #     else:
    #         logger.info("复制机器人重名验证成功!")
    #     One.jqrsc_determine_loc()
    #     One.get_screent_img("Test_jqrsc_3_复制我的机器名称重复")
    #     One.jiqiren_quxiao_loc()
    #     Two.user_tuichu()

    # def test_4(self):
    #     """测试用例4：电话体检-输入电话号码-输入任务名(数字)-点击发送外呼"""
    #     One = jqrsc_page(self.driver)
    #     Two = Login_Page(self.driver)
    #     Three = xtjk_page(self.driver)
    #     Two.user_login(username="test0012", password="111111")
    #     One.jqrsc()
    #     One.phone_number_log()
    #     One.shuru_phone_log('18811730879')
    #     try:
    #         self.assertIn(self.type_jqrsc_phone_error(), "18811730879", msg="失败")
    #     except BaseException as msg:
    #         logger.info("验证失败:%r" %msg)
    #     else:
    #         logger.info("电话体检-输入电话号码验证通过")
    #     def GB2312():
    #         head = random.randint(0x4E00, 0x9FA5)
    #         return head
    #     s = ''
    #     for i in range(2):
    #         s = s + chr(GB2312())
    #     One.jqrsc_rw_log(s)
    #     try:
    #         self.assertIn(self.type_jqrsc_rw_error(), s, msg="失败")
    #     except BaseException as msg:
    #         logger.info("输入任务名(数字)验证失败:%r" %msg)
    #     else:
    #         logger.info("输入任务名(数字)验证成功!")
    #     One.waihu_log()
    #     Three.xitong_jiankong_log()
    #     time.sleep(15)
    #     Two.user_tuichu()

    def test_5(self):
        """测试用例5：电话体检-输入电话号码(>11位,<11位)-输入任务名(数字)-点击发送外呼"""
        One = jqrsc_page(self.driver)
        Two = Login_Page(self.driver)
        Two.user_login(username="test0012", password="111111")
        One.jqrsc()
        One.phone_number_log()
        current_milli_time = lambda: int(round(time.time() * 1000))
        s_time = current_milli_time()
        One.shuru_phone_log_1(s_time)
        try:
            self.assertIn(self.type_jqrsc_phone_error(), s_time, msg="失败")
        except BaseException as msg:
            logger.info("手机号验证失败:%r" %msg)
        else:
            logger.info("手机号验证成功!")

        def GB2312():
            head = random.randint(0x4E00, 0x9FA5)
            return head
        s = ''
        for i in range(2):
            s = s + chr(GB2312())
        self.jqrsc_rw_log_1(s)

        try:
            self.assertIn(self.type_jqrsc_rw_error(),s, msg="失败")
        except BaseException as msg:
            logger.info("验证失败：%r" %msg)
        else:
            logger.info("任务名验证成功")
        One.waihu_log()
        try:
            self.assertEqual(self.type_jqrsc_shuru_phone_log_error(), "手机号输入内容不合法")
        except BaseException as msg:
            logger.info("手机号输入内容不合法验证失败：%r" %msg)
        else:
            logger.info("手机号输入内容不合法验证成功!")
        One.get_screent_img("Test_jqrsc_5_手机号输入内容不合法")
        One.waihu_quxiao_loc()
        Two.user_tuichu()

    def test_6(self):
        """测试用例6：不输入手机号,任务名 点击发起外呼"""
        One = jqrsc_page(self.driver)
        Two = Login_Page(self.driver)
        Two.user_login(username="test0012", password="111111")
        One.jqrsc()
        One.phone_number_log()
        One.waihu_log()
        try:
            self.assertEqual(self.type_jqrsc_null_error(),"手机号不能为空",msg="失败")
        except BaseException as msg:
            print("验证失败!")
            print(" %r" % msg)
        else:
            print("验证成功!")
        One.get_screent_img("Test_jqrsc_6_手机号、任务名输入内容不合法")
        One.waihu_quxiao_loc()
        Two.user_tuichu()

    def test_7(self):
        """测试用例7：输入正确的手机号,任务名 点击发起外呼-发送成功"""
        One = jqrsc_page(self.driver)
        Two = Login_Page(self.driver)
        Three = xtjk_page(self.driver)
        Two.user_login(username="test0012", password="111111")
        One.jqrsc()
        One.phone_number_log()
        One.shuru_phone_log('18811730879')
        try:
            self.assertIn(self.type_jqrsc_phone_error(), "18811730879", msg="失败")
        except BaseException as msg:
            logger.info("验证失败：%r"%msg)
        else:
            logger.info("验证成功!")
        def GB2312():
            head = random.randint(0x4E00, 0x9FA5)
            return head
        s = ''
        for i in range(2):
            s = s + chr(GB2312())
        self.jqrsc_rw_log_1(s)
        try:
            self.assertIn(self.type_jqrsc_rw_error(), s, msg="失败")
        except BaseException as msg:
            logger.info("验证失败:%r" %msg)
        else:
            logger.info("验证成功!")
        One.waihu_log()
        One.get_screent_img("Test_jqrsc_7_外呼发送成功提示")
        try:
            self.assertIn(self.type_jqrsc_waihu_log_error(), "任务创建成功!")
        except BaseException as msg:
            logger.info("验证失败:%r" %msg)
            print("验证失败:%r" %msg)
        else:
            logger.info("验证成功")
            print("验证成功!")
        Three.xitong_jiankong_log()
        One.get_screent_img("Test_jqrsc_7_1_进入系统监控页面查看通话")
        time.sleep(15)
        Two.user_tuichu()

