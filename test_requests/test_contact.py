# -*- coding: utf-8 -*-
# @Time    : 2021/3/27 17:19
# @Author  : Zoey
# @File    : test_contact.py
# @describe:
import requests


class Address:

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
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.get_token()}&userid=zoey"
        r = requests.get(get_member_url)
        assert "Zoey" == r.json()["name"]

    def update_member(self):
        """
        更新成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.get_token()}"
        data = {
            "userid": "zoey",
            "mobile": "15520740912",
            "name": "张张"
        }
        r = requests.post(get_member_url, json=data)

    def create_member(self):
        """
        创建成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.get_token()}"
        data = {
            "userid": "zoey1001",
            "name": "张张2",
            "department": [1],
            "mobile": "15520740912"
        }
        r = requests.post(get_member_url, json=data)
        print(r.json())

    def del_member(self):
        """
        删除成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.get_token()}&userid=zoey1001"
        r = requests.get(get_member_url)
        print(r.json())
