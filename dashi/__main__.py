import tornado

from . import make_app

app = make_app()
app.listen(8080)
tornado.ioloop.IOLoop.current().start()
