# testcases 是一pytets 为测试框架 一个method 就是一个case
from interfaca_frame.testcases.test_base import TestBase


class TestToken(TestBase):

    # def setup(self):
    #     self.gettokn = GetToken()

    def test_get_token(self):
        """调用通用的API"""
        assert self.gettokn.get_token().json()["errcode"] == 0

    def test_get_token_yaml(self):
        """调用封装的 yaml参数"""
        print(self.gettokn.get_token().json())
        assert self.gettokn.get_token_yaml().json()["errcode"] == 0

    def test_get_template_yaml(self):
        """调用封装 template yaml"""
        print(self.gettokn.get_template_yaml().json())
        assert self.gettokn.get_template_yaml().json()["errcode"] == 0