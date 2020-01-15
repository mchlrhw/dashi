from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

from ..model import Dashboard


class DashboardsHandler(SessionMixin, RequestHandler):
    async def get(self):
        with self.make_session() as session:
            await as_future(session.query(Dashboard).count)
        self.write("")
