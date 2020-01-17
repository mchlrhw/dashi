from tornado.web import Application

from .endpoints.dashboards import DashboardHandler, DashboardsHandler
from .endpoints.root import RootHandler


def make_app(db):
    return Application(
        [
            (r"/", RootHandler),
            (r"/dashboards", DashboardsHandler),
            (r"/dashboards/([0-9]+)", DashboardHandler),
        ],
        db=db,
    )
