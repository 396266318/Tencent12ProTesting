from .base_api import BaseApi

# 在API package 中是代表所有的接口信息的具体实现，使用公共方法代表一个接口


class GetToken(BaseApi):

    _corpid = 'ww8444cc2a2443fd63'
    _corpsecret = 'QK4IHS35gm8-E3dw7CY6GeKKrpvrqGzrw6hPzbd-4Bk'

    def get_token(self):
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": self._corpid, "corpsecret": self._corpsecret}}

        r = self.requests_http(req)
        return r


# if __name__ == "__main__":
#     a = GetToken()
#     print(a.get_token().json())
