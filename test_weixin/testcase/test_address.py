# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:02
# @Author  : Zoey
# @File    : test_address.py
# @describe:
from test_weixin.weixin.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.userid = "zoey1001"
        self.name = "张张3"
        self.mobile = "19000000112"
        self.department = [1]

    def test_creat_member(self):
        """
        测试新增员工
        :return:
        """
        self.address.del_member(self.userid)    # 例用删除接口进行数据处理
        r = self.address.create_member(self.userid, self.name, self.mobile, self.department)
        print(r.json()["errmsg"])
        assert r.json()["errmsg"] == "created"
