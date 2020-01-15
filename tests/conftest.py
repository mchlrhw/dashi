import pytest
from tornado_sqlalchemy import SQLAlchemy

from dashi import make_app


@pytest.fixture
def db():
    return SQLAlchemy("mysql://root:test123@127.0.0.1:3306/definitions")


@pytest.fixture
def app(db):
    return make_app(db)
