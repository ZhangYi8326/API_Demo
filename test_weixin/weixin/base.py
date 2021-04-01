# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 17:26
# @Author  : Zoey
# @File    : base.py
# @describe:
import requests


class Base:

    def __init__(self):
        self.s = requests.Session()
        self.token = self.get_token()
        self.s.params = {"access_token": self.token}

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)

    def get_token(self):
        """
        获取token
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww08c6259b12196817&corpsecret=hEoJeNz3yDl6MqIYJK1I4kKdzEqRs1pO-zJDLSaqz4E")
        token = r.json()["access_token"]
        return token