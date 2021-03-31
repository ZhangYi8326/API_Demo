# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:02
# @Author  : Zoey
# @File    : test_address.py
# @describe:
import pytest

from test_weixin.weixin.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.userid = "zoey1001"
        self.name = "张张3"
        self.mobile = "19000000112"
        self.department = [1]

    @pytest.mark.parametrize("user_id, name, mobile", [
        ("zhangsnag001", "张三001", "15711111111"),
        ("zhangsnag002", "张三002", "15722222222"),
        ("zhangsnag003", "张三003", "15733333333"),
        ("zhangsnag004", "张三004", "15744444444"),
        ("zhangsnag005", "张三005", "15755555555"),
        ("zhangsnag006", "张三006", "15766666666"),
        ("zhangsnag007", "张三007", "15777777777"),
        ("zhangsnag008", "张三008", "15788888888")
    ])
    def test_create_member(self, user_id, name, mobile):
        """
        测试新增员工
        :return:
        """
        self.address.del_member(user_id)    # 例用删除接口进行数据处理
        r = self.address.create_member(user_id, name, mobile, self.department)
        assert r.json()["errmsg"] == "created"
        r = self.address.get_member_info(user_id)
        assert r.get("name") == name

    def test_get_member_info(self):
        """
        测试读取成员
        :return:
        """
        r = self.address.get_member_info(self.userid)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == self.name

    def test_del_member(self):
        """
        删除成员测试用例
        :return:
        """
        r = self.address.del_member(self.userid)
        assert r.get("errmsg") == "deleted"
        r = self.address.get_member_info(self.userid)
        assert r.get("errcode") == 60111

    def test_update_member(self):
        """
        更新成员操作
        :return:
        """
        self.address.del_member(self.userid)
        self.address.create_member(self.userid, self.name, self.mobile, self.department)
        new_name = self.name + "temp"
        r = self.address.update_member(self.userid, new_name, self.mobile)
        assert r.get("errmsg") == "updated"
        r = self.address.get_member_info(self.userid)
        assert r.get("name") == new_name
