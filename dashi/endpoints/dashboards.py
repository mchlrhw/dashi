import json

from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

from ..model import Dashboard


def dashboard_to_json(row):
    json_obj = {
        "id": row.id,
        "createdAt": row.createdAt.isoformat(),
        "updatedAt": row.updatedAt.isoformat(),
        "title": row.title,
    }
    return json_obj


class DashboardsHandler(SessionMixin, RequestHandler):
    async def get(self):
        with self.make_session() as session:
            dashboards = await as_future(session.query(Dashboard).all)
            serializable = [dashboard_to_json(row) for row in dashboards]

        payload = json.dumps(serializable)
        self.write(payload)
