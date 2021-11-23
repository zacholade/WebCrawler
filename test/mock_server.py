from collections import defaultdict

from aiohttp import web


class MockServer:
    def __init__(self):
        self.app = web.Application()
        self.app.add_routes([
            web.get('/', self.index),
            web.get('/foo', self.foo),
            web.get('/bar', self.bar)
        ])

        # A dictionary to count the number of times each route is requested.
        self.route_counter = defaultdict(int)

    def increment(self, route: str):
        self.route_counter[route] += 1

    async def index(self, request):
        self.increment('/')

        return web.Response(
            text='<h1>Hello World!</h1><a href="https://www.foo.com/">This is a website</a>',
            content_type='text/html')

    async def foo(self, request):
        self.increment('/foo')
        # TODO

    async def bar(self, request):
        self.increment('/foo')
        # TODO