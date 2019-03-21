import asyncio
import logging
from time import time

from tornado.httpserver import HTTPServer
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.web import Application
from tornado.web import RequestHandler


logger = logging.getLogger(__name__)


class TestHandler(RequestHandler):

    def post(self):
        print(self.request)
        print(self.request.full_url())
        print(self.request.method)
        print(self.request.uri)
        print(self.request.remote_ip)
        print(self.request.host)
        print(self.request.body)
        print(self.path_args)
        print(self.get_status())
        logger.info('request received')

    def get(self):
        print(self.request.full_url())
        print(self.request.arguments)
        print('#####')
    # Lifecycle

    def prepare(self):
        self.start_time = time()

    def on_finish(self):
        tornado_time = self.request.request_time()
        logger.info(f'Tornado says request took {tornado_time} s')

        my_time = time() - self.start_time
        logger.info(f'I say it took {my_time} s')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    AsyncIOMainLoop().install()

    app = Application(
        handlers=[('/a', TestHandler)],
        autoescape=None,
        debug=True,
    )

    server = HTTPServer(app)
    server.listen(8080)

    loop = asyncio.get_event_loop()
    loop.run_forever()