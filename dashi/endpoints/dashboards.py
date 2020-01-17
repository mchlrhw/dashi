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

    async def post(self):
        payload = json.loads(self.request.body)
        title = payload["title"]

        with self.make_session() as session:
            row = Dashboard(title=title)
            await as_future(lambda: session.add(row))
            session.flush()
            session.refresh(row)
            row_id = row.id

        response = {"id": row_id}
        resp_payload = json.dumps(response)
        self.write(resp_payload)


class DashboardHandler(SessionMixin, RequestHandler):
    async def get(self, dash_id):
        with self.make_session() as session:
            row = await as_future(lambda: session.query(Dashboard).get(dash_id))
            if row is None:
                raise HTTPError(404)
            serializable = dashboard_to_json(row)

        payload = json.dumps(serializable)
        self.write(payload)
