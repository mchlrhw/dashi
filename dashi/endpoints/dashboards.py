import json

from tornado.web import HTTPError, RequestHandler
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


class DashboardHandler(SessionMixin, RequestHandler):
    async def get(self, dash_id):
        with self.make_session() as session:
            row = await as_future(lambda: session.query(Dashboard).get(dash_id))
            if row is None:
                raise HTTPError(404)
            serializable = dashboard_to_json(row)

        payload = json.dumps(serializable)
        self.write(payload)
