# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/3 16:05
@Auth ： Zoey
@File ：run.py
@Description：运行入口
"""
import pytest


# pytest.main(["./testcase/test_address.py"])
pytest.main(["-s", "-q", "--alluredir=./result/5"])
