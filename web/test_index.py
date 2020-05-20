# -*- coding: utf-8 -*-
import time
import pytest
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_xiugai_time(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        time.sleep(3)


if __name__ == "__main__":
    # pytest.main(['-vs', 'test_index.TestDemo::test_xiugai_time'])
    # a = TestDemo()
    # a.test_xiugai_time()
    unittest.main()


