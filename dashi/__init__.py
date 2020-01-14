from tornado.web import Application

from .endpoints.dashboards import DashboardsHandler
from .endpoints.root import RootHandler


def make_app():
    return Application([("/", RootHandler), ("/dashboards", DashboardsHandler)])
