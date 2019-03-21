# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 20:58
# @Author  : RIO
# @desc: 测试逻辑部分
from athena.biz.algorithm import test_algorithm


def test_biz():
    return "##athena.biz.test_biz.test_biz" + test_algorithm.test_algo()
