import requests
import json

corpid = 'ww8444cc2a2443fd63'
corpsecret = 'QK4IHS35gm8-E3dw7CY6GeKKrpvrqGzrw6hPzbd-4Bk'
# corpsecret = 'XHwdkDdSiTcZbpmImgO51vN8rotbMdcKi4pvAH63E3Y'


def token():
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")
    text = json.loads(res.text)
    token = text.get("access_token")
    return token

print(token())

def test_query_department():
    """查询部门"""
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token()}")
    print(res.text)


def test_add_department():
    """添加部门"""
    data = {
        "name": "广州研发中心",
        "name_en": "RDGZ",
        "parentid": 2,
        "order": 1,
    }

    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={token()}", json=data)
    print(res.text)


def test_update_department():
    """更新部门"""
    data = {"id": 2, "name": "测试部门3", "parentid": 1, "order": 100000000}
    res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={token()}", json=data)
    print(res.text)


def test_delete_department():
    """删除部门"""
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token()}&id=2")
    print(res.text)