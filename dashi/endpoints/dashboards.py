from tornado.web import RequestHandler


class DashboardsHandler(RequestHandler):
    def get(self):
        self.write("")
