# -*- coding: utf-8 -*-
# @Time    : 2018/11/13  11:26
# @Author  : 陆平！！
# @FileName: test_3__case.py.py
# @Software: PyCharm

import time
import unittest
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_login import Login_Page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_wdjqr import wdjqr_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.ruisi_object_jqrsc import jqrsc_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_whrw import whrw_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_xtjk import xtjk_page
from AICC.aicc_Cloud.aicc_Plu.aicc_plu_screenshots.screenshots_wdjqr import wdjqr_screenshots


class Test_wdjqr_model(wdjqr_screenshots,Login_Page,wdjqr_page,jqrsc_page,whrw_page,xtjk_page):

    def user_login_verify(self,username="",password=""):
        self.login_page.user_login(username,password)

    def test_1(self):
        '''测试用例1：进入我的机器人页面 并截图'''
        self.user_login_verify(username="test0012",password="111111")
        time.sleep(1)
        self.wdjqr_robot_log()
        if self.type_wdjqr_title() == "我的机器人":
            print("验证成功")
        else:
            print("验证失败")
        time.sleep(0.5)
        self.wdjqr_jietu_case_1()
        time.sleep(0.5)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(0.5)
        self.quitqueding()
        time.sleep(1)

    def test_2(self):
        '''测试用例2：进入我的机器人页面-查看参数 并截图'''
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.wdjqr_robot_log()
        if self.type_wdjqr_title() == "我的机器人":
            print("验证成功")
        else:
            print("验证失败")
        time.sleep(0.5)
        self.wdjqr_ckcs_log()
        time.sleep(2)
        self.wdjqr_jietu_case_2()
        self.wdjqr_ckcs_gb_log()
        time.sleep(1)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(0.5)
        self.quitqueding()
        time.sleep(2)

    def test_3(self):
        '''测试用例3：进入我的机器人页面-查看短信 并截图'''
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.wdjqr_robot_log()
        if self.type_wdjqr_title() == "我的机器人":
            print("验证成功")
        else:
            print("验证失败")
        time.sleep(0.5)
        self.wdjqr_ckdx_log()
        time.sleep(2)
        self.wdjqr_jietu_case_3()
        if self.type_wdjqr_ckdx_title() == "短信模板":
            print("成功")
        else:
            print("失败")
        self.driver.back()
        time.sleep(1)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(0.5)
        self.quitqueding()
        time.sleep(2)

    def test_4(self):
        '''测试用例4：在我的机器人页面-正常外呼'''
        self.user_login_verify(username="test0012",password="111111")
        time.sleep(2)
        self.wdjqr_robot_log()
        if self.type_wdjqr_title() == "我的机器人":
            print("认证成功")
        else:
            print("认证失败")
        self.wdjqr_zhwh_log()
        time.sleep(2)
        self.wdjqr_phone_log()
        self.wdjqr_rw_name_log()
        time.sleep(2)
        self.wdjqr_fqwh_log()
        time.sleep(1)
        self.wdjqr_jietu_case_4()
        time.sleep(0.5)
        self.xitong_jiankong_log()
        time.sleep(20)
        self.task_log()
        time.sleep(2)
        self.task_ckxq_log()
        self.task_ckxq_ckxq_log()
        time.sleep(2)
        self.task_ckxq_ckxq_bfly_log()
        time.sleep(15)
        self.task_ckxq_ckxq_gb_log()
        time.sleep(2)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(1)
        self.quitqueding()
        time.sleep(2)


    def test_5(self):
        '''测试用例5：复制机器人ID'''
        self.user_login_verify(username="test0012",password="111111")
        time.sleep(1)
        self.wdjqr_robot_log()
        try:
            self.assertEqual(self.wdjqr_name_log(),self.jqrsc_name_loc(),msg="验证失败")
        except BaseException as msg:
            print("验证失败！")
            print(" %s" %msg)
        else:
            print("验证通过！")
        time.sleep(1)
        self.wdjqr_ID_log()
        time.sleep(0.5)
        self.wdjqr_jietu_case_5()
        try:
            self.assertIn(self.type_wdjqr_ID_return(),"复制成功",msg="验证失败")
        except BaseException as msg:
            print("验证失败！")
            print(" %s" % msg)
        else:
            print("验证通过！")
        time.sleep(3)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(1)
        self.quitqueding()
        time.sleep(2)

    def test_6(self):
        '''测试用例6：批量外呼-查看详情-录音播放-导出明细'''
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.wdjqr_robot_log()
        try:
            self.assertEqual(self.wdjqr_name_log(), self.jqrsc_name_loc(), msg="验证失败")
        except BaseException as msg:
            print("验证失败！")
            print(" %s" % msg)
        else:
            print("验证通过！")
        time.sleep(1)
        self.wdjqr_pl_wh_log()
        self.wdjqr_pl_wd_xqwj_log()
        time.sleep(4)
        self.wdjqr_jietu_case_6_1()
        self.wdjqr_pl_wh_xqwj_rwm_log()
        time.sleep(2)
        self.wdjqr_pl_wh_xqwj_rwm_fqwh_log()
        time.sleep(4)
        self.xitong_jiankong_log()
        time.sleep(30)
        self.task_log()
        time.sleep(2)
        self.task_ckxq_log()
        self.task_ckxq_ckxq_log()
        time.sleep(2)
        self.task_ckxq_ckxq_bfly_log()
        time.sleep(0.5)
        self.wdjqr_jietu_case_6_2()
        time.sleep(14)
        self.task_ckxq_ckxq_gb_log()
        time.sleep(2)
        self.task_dcmx_log()
        self.wdjqr_jietu_case_6_3()
        time.sleep(9)
        self.wdjqr_jietu_case_6_4()
        time.sleep(2)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(0.5)
        self.quitqueding()
        time.sleep(2)

    def test_7(self):
        '''测试用例7：进入我的机器人页面-复制版本 '''
        self.user_login_verify(username="test0012", password="111111")
        time.sleep(1)
        self.wdjqr_robot_log()
        if self.type_wdjqr_title() == "我的机器人":
            print("验证成功")
        else:
            print("验证失败")
        time.sleep(0.5)
        self.wdjqr_fzbb_log()
        time.sleep(1)
        self.wdjqr_fzbb_qd_log()
        try:
            self.assertIn(self.wdjqr_fzbb_asser,"复制新版本成功",msg="复制失败")
        except BaseException as msg:
            print("验证失败")
            print("%r" %msg)
        else:
            print("复制成功")
        time.sleep(1)
        self.wdjqr_jietu_case_7()
        time.sleep(1)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(2)
        self.quitqueding()
        time.sleep(2)
