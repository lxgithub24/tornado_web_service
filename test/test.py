from time import sleep

import requests


class SlowFile:

    lines = [
        b'Now is the time',
        b'for all good men',
        b'to come to the aid',
        b'of their country',
    ]

    def __iter__(self):
        for l in type(self).lines:
            # sleep(2)
            # print(l)
            yield l


def main():
    f = SlowFile()
    # import json
    # print(json.loads(f))
    requests.get('http://localhost:8080/a?a=1')


if __name__ == '__main__':
    main()