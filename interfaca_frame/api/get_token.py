import requests
import json

# corpsecret = 'XHwdkDdSiTcZbpmImgO51vN8rotbMdcKi4pvAH63E3Y'
# def token():
#     corpid = 'ww8444cc2a2443fd63'
#     corpsecret = 'QK4IHS35gm8-E3dw7CY6GeKKrpvrqGzrw6hPzbd-4Bk'
#     res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
#     text = json.loads(res.text)
#     token = text.get("access_token")
#     return token


# print(token())


class GetToken:
    _corpid = 'ww8444cc2a2443fd63'
    _corpsecret = 'QK4IHS35gm8-E3dw7CY6GeKKrpvrqGzrw6hPzbd-4Bk'

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self._corpid,
            "corpsecret": self._corpsecret
        }
        r = requests.get(url=url, params=params)
        # print(r.json().get("access_token"))
        # return r.json().get("access_token")
        return r


if __name__ == "__main__":
    a = GetToken()
    a.get_token()
