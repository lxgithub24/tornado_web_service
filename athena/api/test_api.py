# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 16:11
# @Author  : RIO
# @desc: 测试接口
import tornado.web
from athena.biz import test_biz

from athena.utils.handler.prerequest import BaseHandler


class BaseTest(BaseHandler):
    def get(self):
        content = {"key": test_biz.test_biz()}
        self.write(self.success_response(content))

    def post(self):
        pass

    def delete(self):
        pass
