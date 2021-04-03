# -*- coding: utf-8 -*-
"""
@Time ： 2021/4/3 14:34
@Auth ： Zoey
@File ：read_data.py
@Description：读取数据并返回数据
"""
import yaml


class ReadData:

    def read_data(self, path, function):
        """
        读取文件内容并返回
        :param path: 要读取的文件路径
        :param function: 读取数据的方法
        :return:
        """
        with open(path, "r", encoding="utf-8") as f:
            datas = yaml.safe_load(f)[function] # 获取数据，返回类型list:list
            return datas


if __name__ == '__main__':
    ReadData().read_data("../data/test_data.yaml", "create_member")
