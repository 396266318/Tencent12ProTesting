from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddMember:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_member(self):
        sleep(2)
        self._driver.find_element(By.ID, "username").send_keys("abceffffff")
        self._driver.find_element(By.ID, "memberAdd_english_name").send_keys("abcdeffff")

        self._driver.find_element(By.ID, "memberAdd_phone").send_keys("1122222222")
        sleep(5)
        self._driver.quit()
        return True