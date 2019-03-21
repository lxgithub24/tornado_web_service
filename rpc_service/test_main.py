# coding: utf8
from athena.utils.middleware.misc import register_signal_hanlder
from athena.utils.middleware.lion import zk_register, get_property_from_zk
from rpc_service.rpc_server import algorithm_server
from rpc_service.pb_api import test_pb2_grpc
from concurrent import futures
import socket
import grpc
import time
import sys

sys.path.append('/data/apps/athena/current/')

if len(sys.argv) != 3:
    print('err args')
    sys.exit(0)

host = sys.argv[1]
port = int(sys.argv[2])
SERVICE_NAME = {'ATHENA_DEFAULT': 'path', 'ATHENA_SERVICENAME': get_property_from_zk(
    'ATHENA_SERVICENAME')}.get('ATHENA_DEFAULT')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    register_signal_hanlder(server)
    test_pb2_grpc.add_TestServiceServicer_to_server(
        algorithm_server.TestService(), server)
    server.add_insecure_port('[::]:%s' % port)

    # 注册到zk上
    zk_register(SERVICE_NAME, host + ":" + port)

    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
