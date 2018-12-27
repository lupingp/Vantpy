# -*- coding: utf-8 -*-
# @Time    : 2018/11/14  15:24
# @Author  : 陆平！！
# @FileName: test_4_whrw_case.py
# @Software: PyCharm

import time
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_login import Login_Page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_wdjqr import wdjqr_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_whrw import whrw_page
from AICC.aicc_Cloud.aicc_Project.aicc_Object.rusi_object_xtjk import xtjk_page
from AICC.aicc_Cloud.aicc_Plu.aicc_plu_screenshots.screenshots_whrw import whrw_screenshots

class Test_whrw_model(whrw_screenshots,Login_Page,wdjqr_page,whrw_page):

    def user_login_verify(self,username="",password=""):
        self.login_page.user_login(username="test0012",password="111111")

    def test_1(self):
        '''测试用例1：批量选中-选中导出'''
        self.user_login_verify()
        self.task_log()
        if self.task_assert_log() == "外呼任务":
            print("验证成功")
        else:
            print("验证失败")
        time.sleep(1)
        self.task_pldc_mx_log()
        time.sleep(2)
        self.task_pldc_mx_xzdc_log()
        time.sleep(2)
        self.whrw_jietu_case_1()
        time.sleep(8)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(1)
        self.quitqueding()
        time.sleep(2)

    def test_2(self):
        '''测试用例2：外呼任务-重置成功'''
        self.user_login_verify()
        self.task_log()
        time.sleep(1)
        self.task_whrw_rwzt_log()
        time.sleep(2)
        self.task_whrw_rwzt_xz_log()
        self.task_cx_log()
        time.sleep(0.5)
        self.whrw_jietu_case_2_1()
        time.sleep(2)
        self.task_cz_log()
        self.whrw_jietu_case_2_2()
        time.sleep(3)
        self.tuichu()
        time.sleep(1)
        self.quitloc()
        time.sleep(2)
        self.quitqueding()
        time.sleep(2)
