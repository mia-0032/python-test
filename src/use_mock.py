# -*- coding:utf-8 -*-

import unittest
from mock import Mock, patch


# DBにつなぐのでテストのときは使いたくないクラス
class HogehogeDao(object):
    def __init__(self):
        pass

    def find(self, param_1, param_2):
        print('DBにつなぐよ')
        print('find ' + param_1 + param_2)


# テストの対象となるクラス
class CalculationModel(object):
    def __init__(self, dao):
        self.__dao = dao

    def execute(self):
        return self.__dao.find('hoge', param_2='foo')

# 使い方
if __name__ == '__main__':
    calc = CalculationModel(HogehogeDao())
    calc.execute()
    # DBにつなぐよ
    # find hogefoo
    # と表示される。
