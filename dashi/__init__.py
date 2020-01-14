from tornado.web import Application, RequestHandler

from .endpoints.dashboards import DashboardsHandler


class RootHandler(RequestHandler):
    def get(self):
        self.write("🍲")


def make_app():
    return Application([("/", RootHandler), ("/dashboards", DashboardsHandler)])
