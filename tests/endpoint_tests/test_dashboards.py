import json
from urllib.parse import urljoin

import pytest


@pytest.mark.gen_test
async def test_dashboards(http_client, base_url):
    dashboards_url = urljoin(base_url, "/dashboards")

    resp = await http_client.fetch(dashboards_url)
    assert resp.code == 200

    payload = json.loads(resp.body)

    assert "id" in payload
    assert payload["id"] > 0

    assert "createdAt" in payload
    assert payload["createdAt"]

    assert "updatedAt" in payload
    assert payload["updatedAt"]

    assert "title" in payload
    assert payload["title"]
