import tornado
from tornado_sqlalchemy import SQLAlchemy

from . import make_app

db = SQLAlchemy("mysql://root:test123@mysql-db:3306/definitions")
app = make_app(db)
app.listen(8080)
tornado.ioloop.IOLoop.current().start()
