from time import sleep

from selenium.webdriver.common.by import By
from selenium_wework_main.page.base_page import BasePage


class AddMember(BasePage):
    """通讯录添加成员功能"""

    def add_member(self):
        """添加成员"""
        self.find(By.ID, "username").send_keys("abcdeffffff")
        self.find(By.ID, "memberAdd_acctid").send_keys("abcdeffffff")
        self.find(By.ID, "memberAdd_acctid").send_keys("abcdeffffff")
        self.find(By.ID, "memberAdd_phone").send_keys("11111111111")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()

    def update_page(self):
        """更新页面"""
        content: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
        # 对 1/10 页进行切割
        return [int(x) for x in content.split('/', 1)]

    def get_member(self, value):
        """获取通讯录添加的联系人名称"""
        self.wait_for_click((By.CSS_SELECTOR, ".ww_checkbox"))
        cur_page, total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
            for element in elements:
                if value == element.get_attribute("title"):
                    return True
            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, ".js_next_page").click()
