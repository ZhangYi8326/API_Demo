# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:01
# @Author  : Zoey
# @File    : address.py
# @describe:
import requests


class Address:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        """
        获取token
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww08c6259b12196817&corpsecret=hEoJeNz3yDl6MqIYJK1I4iO7fqz3zQlv8PFB73HH8CM")
        token = r.json()["access_token"]
        return token

    def defect_member(self):
        """
        读取成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=zoey"
        r = requests.get(get_member_url)
        assert "Zoey" == r.json()["name"]

    def update_member(self):
        """
        更新成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "zoey",
            "mobile": "15520740912",
            "name": "张张"
        }
        r = requests.post(get_member_url, json=data)

    def create_member(self, userid, name, mobile, department):
        """
        创建成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        r = requests.post(get_member_url, json=data)
        return r

    def del_member(self, userid):
        """
        删除成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            "access_token": self.token,
            "userid": userid
        }
        r = requests.get(get_member_url, params=params)
        return r.json()
