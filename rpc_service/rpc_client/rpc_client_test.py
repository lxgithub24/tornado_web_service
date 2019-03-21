# from __future__ import print_function
# coding:utf8

import sys

sys.path.append("/data/apps/fav_site/current/")

import json
import grpc
from rpc_service.pb_api import test_pb2_grpc, test_pb2
from athena.utils.middleware.lion import get_property_from_zk

# 服务发现：TODO:√

rpc_url = "{}:{}".format('127.0.0.1', '8080')
channel = grpc.insecure_channel(rpc_url)

test_stub = test_pb2_grpc.TestServiceStub(channel)


def test_client(id):
    response = test_stub.test(test_pb2.TestRequest(id=id))
    return json.loads(response.result) if response else {}


if __name__ == '__main__':
    print(test_client("558479031"))
