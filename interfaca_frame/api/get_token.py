from string import Template

import yaml

from .base_api import BaseApi

# 在API package 中是代表所有的接口信息的具体实现，使用公共方法代表一个接口


class GetToken(BaseApi):

    _corpid = 'ww8444cc2a2443fd63'
    _corpsecret = 'QK4IHS35gm8-E3dw7CY6GeKKrpvrqGzrw6hPzbd-4Bk'

    def template(self):
        """调用模板处理传参数据"""
        with open("../api/get_token.yaml") as f:
            data = {
                "corpid": self._corpid,
                "corpsecret": self._corpsecret
            }
            # re = Template(f.read()).substitute(corpid=self._corpid, corpsecret=self._corpsecret)
            re = Template(f.read()).substitute(data)
            return yaml.safe_load(re)

    def get_token(self):
        """获取token"""
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": self._corpid, "corpsecret": self._corpsecret}}

        r = self.requests_http(req)
        return r

    def get_token_yaml(self):
        """调用yaml入参方式获取token"""
        req = yaml.safe_load(open("../api/get_token.yaml"))
        r = self.requests_http(req)
        return r

    def get_template_yaml(self):
        """调用封装的 template 传递参数 """
        req = self.template()
        r = self.requests_http(req)
        return r




# if __name__ == "__main__":
#     a = GetToken()
#     # print(a.get_token().json())
#     a.template()