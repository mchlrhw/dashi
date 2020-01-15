import json
from urllib.parse import urljoin

import pytest


@pytest.mark.gen_test
async def test_dashboards(http_client, base_url):
    dashboards_url = urljoin(base_url, "/dashboards")

    resp = await http_client.fetch(dashboards_url)
    assert resp.code == 200

    payload = json.loads(resp.body)
    first = payload[0]

    assert "id" in first
    assert first["id"] > 0

    assert "createdAt" in first
    assert first["createdAt"]

    assert "updatedAt" in first
    assert first["updatedAt"]

    assert "title" in first
    assert first["title"]
