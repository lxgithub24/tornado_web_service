# -*- coding: utf-8 -*-
# @Time    : 2018/11/3 10:52
# @Author  : RIO
# @desc: test server

from rpc_service.pb_api import test_pb2_grpc, test_pb2
try:
    import ujson as json
except:
    import json


class TestService(test_pb2_grpc.TestServiceServicer):

    def test(self, request, context):
        code, res = 'ok', {}
        response = test_pb2.TestResponse()
        if code == 'ok':
            response.res = json.dumps(res)
        else:
            response.res = ''
        return response