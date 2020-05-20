# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9223"

        # self.driver = webdriver.Chrome(options=options) # 浏览器复用
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element(By.LINK_TEXT, "分类").click()
        sleep(5)

    def test_wework(self):
        """复用浏览器点击企业微信的通讯录"""
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.LINK_TEXT, "通讯录").click()
        sleep(5)

    def test_cook(self):
        """使用浏览器 cookis 登录"""
        cookies = [{'domain': '.qq.com', 'expiry': 1589968936, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850485462278'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'YJbIYiioYUhIn7GldtRk_G-37-YXusHqZ2EF5kNNbzTtQ-_BDxXRwGwxsQzRb82FO2QBV_ikPxiEOycEK_VMQmLD1R_4Da8-zu4nRq4R2u0WXMDznYuH5oxXuwljJyYL_3cj-xwtKi_RKbWhJTTdVCrCFBiUX2xSL1DmNCWvoMHYXjQl28cmvnYEYY7Y93jf8m2YfYVASx4aBbb5WLruKd4aHYBiqHr1fDjvBmTO2JaoN7ohFJ65I0tLfwiblv09X9V_d9QRq9VZsbuUgUmKNg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621504706, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1589968603,1589968707'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3001878'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325004131500'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850485462278'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1590055141, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2104828510.1589968603'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '1692638279'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1589968707'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '40765343303402446'}, {'domain': '.qq.com', 'expiry': 1653040741, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.265920559.1589968603'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'UQcS1aBAwDDJYOwMv9BMnEo4Qo4JGf73lal21je7wJikxZXG55HGXQ2W2XScjvVe'}, {'domain': '.work.weixin.qq.com', 'expiry': 1592560878, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(3)
