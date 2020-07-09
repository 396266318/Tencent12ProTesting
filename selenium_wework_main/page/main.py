from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_main.page.add_member import AddMember
from selenium_wework_main.page.base_page import BasePage


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def goto_add_member(self):
        self.find(By.ID, "menu_contacts").click()  # 点击通讯录
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")  # 点击添加成员
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        return AddMember(self._driver)

        def wait_add_member(x):
            elements_len = len(self.find(By.CSS_SELECTOR, "#username"))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
            return elements_len > 0
        self.wait_for_elem(wait_add_member)
        return AddMember(self._driver)

