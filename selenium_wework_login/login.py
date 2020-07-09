from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wework_login.register import Register


class Login:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver

    def scanf(self):
        pass

    def goto_register(self):
        # click
        self._driver.find_element(By.CSS_SELECTOR, ".login_registerBar_link").click()

        return Register(self._driver)
