# -*- coding:utf-8 -*-

from grpc_tools import protoc

protoc.main(
    (
        '',
        '-I../proto_buffer_config',
        '--python_out=../pb_api',
        '--grpc_python_out=../pb_api',
        '../proto_buffer_config/test.proto',
    ),

    # (
    #     '',
    #     '-I./grpc_protos',
    #     '--python_out=./pb',
    #     '--grpc_python_out=./pb',
    #     './grpc_protos/user_info.proto',
    # )


# python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. helloworld.proto
)
