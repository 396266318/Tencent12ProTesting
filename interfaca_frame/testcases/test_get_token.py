# from api.get_token import GetToken
from interfaca_frame.api.get_token import GetToken

# testcases 是一pytets 为测试框架 一个method 就是一个case


class TestToken:

    def setup(self):
        self.gettokn = GetToken()

    def test_get_token(self):
        # print("ddd")
        assert self.gettokn.get_token().json()["errcode"] == 0