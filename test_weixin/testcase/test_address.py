# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 17:02
# @Author  : Zoey
# @File    : test_address.py
# @describe: 通讯录测试用例
import pytest
import allure

from test_weixin.weixin.address import Address
from test_weixin.comm.read_data import ReadData


@allure.feature("通讯录模块测试用例")
class TestAddress(ReadData):
    create_member = ReadData().read_data("./data/test_data.yaml", "create_member")
    get_member = ReadData().read_data("./data/test_data.yaml", "get_member")
    del_member = ReadData().read_data("./data/test_data.yaml", "del_member")
    update_member = ReadData().read_data("./data/test_data.yaml", "update_member")

    def setup_class(self):
        self.address = Address()

    @pytest.mark.parametrize("user_id, name, mobile, department", create_member)
    @allure.story("新增员工测试用例")
    def test_create_member(self, user_id, name, mobile, department):
        """
        测试新增员工
        :return:
        """
        self.address.del_member(user_id)    # 利用删除接口进行数据处理
        r = self.address.create_member(user_id, name, mobile, department)
        assert r.get("errmsg", "network error") == "created"
        r = self.address.get_member_info(user_id)
        assert r.get("name") == name

    @pytest.mark.parametrize("user_id, name", get_member)
    @allure.story("读取成员测试用例")
    def test_get_member_info(self, user_id, name):
        """
        测试读取成员
        :return:
        """
        r = self.address.get_member_info(user_id)
        assert r.get("errmsg") == "ok"
        assert r.get("name") == name

    @pytest.mark.parametrize("userid, name, mobile, department", del_member)
    @allure.story("删除成员测试用例")
    def test_del_member(self, userid, name, mobile, department):
        """
        删除成员测试用例
        :return:
        """
        self.address.create_member(userid, name, mobile, department)    # 删除之前先进行创建操作
        r = self.address.del_member(userid)     # 删除成员操作
        assert r.get("errmsg") == "deleted"
        r = self.address.get_member_info(userid)   # 读取成员不存在
        assert r.get("errcode") == 60111

    @pytest.mark.parametrize("userid, name, mobile, department", update_member)
    @allure.story("更新成员测试用例")
    def test_update_member(self, userid, name, mobile, department):
        """
        更新成员操作
        :return:
        """
        self.address.del_member(userid)    # 先执行删除操作
        self.address.create_member(userid, name, mobile, department)    # 再执行创建操作
        new_name = name + "temp"
        r = self.address.update_member(userid, new_name, mobile)    # 执行更新操作
        assert r.get("errmsg") == "updated"
        r = self.address.get_member_info(userid)    # 读取成员，判断更新后的姓名是否正确
        assert r.get("name") == new_name
