# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:01
# @Author  : Zoey
# @File    : address.py
# @describe: 借口封装

from test_weixin.weixin.base import Base


class Address(Base):
    def get_member_info(self, userid):
        """
        读取成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?"
        params = {
            "userid": userid
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()

    def update_member(self, user_id, name, mobile):
        """
        更新成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": user_id,
            "mobile": mobile,
            "name": name
        }
        r = self.send("POST", get_member_url, json=data)
        return r.json()

    def create_member(self, userid, name, mobile, department):
        """
        创建成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "department": department,
            "mobile": mobile
        }
        r = self.send("POST", get_member_url, json=data)
        return r.json()

    def del_member(self, userid):
        """
        删除成员
        :return:
        """
        get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            "userid": userid
        }
        r = self.send("GET", get_member_url, params=params)
        return r.json()
