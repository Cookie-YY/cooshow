from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from app import app
from tornado.ioloop import IOLoop

s = HTTPServer(WSGIContainer(app))
s.listen(3392)  # 监听 3389 端口
IOLoop.current().start()
