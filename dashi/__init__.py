import tornado
from tornado.web import Application, RequestHandler


class RootHandler(RequestHandler):
    def get(self):
        self.write("🍲")


def make_app():
    return Application([("/", RootHandler)])
