from typing import TYPE_CHECKING

from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.sql.functions import now
from tornado_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
if TYPE_CHECKING:
    Model = object
else:
    Model = db.Model


class Dashboard(Model):
    __tablename__ = "dashboards"

    id = Column(BigInteger, primary_key=True)
    createdAt = Column(DateTime, nullable=False, default=now())
    updatedAt = Column(DateTime, nullable=False, default=now(), onupdate=now())
    title = Column(String, nullable=False)
