import json

from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

from ..model import Dashboard


class DashboardsHandler(SessionMixin, RequestHandler):
    async def get(self):
        with self.make_session() as session:
            dashboards = await as_future(session.query(Dashboard).all)

        serializable = [d.__dict__ for d in dashboards]
        payload = json.dumps(serializable)

        self.write(payload)
