import pytest


@pytest.mark.gen_test
async def test_root(http_client, base_url):
    resp = await http_client.fetch(base_url)
    assert resp.code == 200
