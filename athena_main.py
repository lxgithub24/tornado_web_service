# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 16:06
# @Author  : RIO
# @desc: 系统入口
import tornado.ioloop
import tornado.web
import tornado.httpserver
import asyncio
import os
import sys
from wasp_eureka import EurekaClient

from athena.api.test_api import BaseTest
from athena.utils.config import config
from athena.utils.handler import prerequest

port = int(sys.argv[1])

rest_apis_handler = [(r"/athena/test", BaseTest), ]


loop = asyncio.get_event_loop()  # 创建事件循环

eureka = EurekaClient(
    app_name=config.APP_NAME,
    port=port,
    ip_addr=config.HOST_IP,
    hostname=config.HOST_IP,
    eureka_url=config.REGISTER_EUREKA_HOST,
    loop=loop)


async def main():
    result = await eureka.register()
    print("[Register Rureka] result: %s" % result)
    app = tornado.web.Application(handlers=rest_apis_handler)
    server = tornado.httpserver.HTTPServer(app, idle_connection_timeout=31536000000)
    server.listen(port)
    prerequest.smooth_reload(server)
    while True:
        await asyncio.sleep(60)
        await eureka.renew()


if __name__ == '__main__':
    loop.run_until_complete(main())