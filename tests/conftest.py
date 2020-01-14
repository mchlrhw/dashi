import pytest

from dashi import make_app


@pytest.fixture
def app():
    return make_app()
