import pytest

from dashi import make_app


@pytest.fixture
def app():
    return make_app()


@pytest.mark.gen_test
async def test_root(http_client, base_url):
    resp = await http_client.fetch(base_url)
    assert resp.code == 200
