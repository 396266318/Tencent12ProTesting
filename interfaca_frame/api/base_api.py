import requests


class BaseApi:

    def requests_http(self, req):
        """封装基础 requests http 请求"""
        r = requests.request(**req)
        # print(r.json())
        return r