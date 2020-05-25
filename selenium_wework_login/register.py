from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):
        # send content
        # click element
        sleep(3)
        self._driver.find_element(By.ID, "corp_name").send_keys("Hello1111")
        self._driver.find_element(By.ID, "manager_name").send_keys("Hello0001")
        sleep(3)
        self._driver.quit()
        return True
    