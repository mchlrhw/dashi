import json
from urllib.parse import urljoin

import pytest
from tornado.httpclient import HTTPClientError, HTTPRequest


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


@pytest.mark.gen_test
async def test_dashboard(http_client, base_url):
    dashboard_url = urljoin(base_url, "/dashboards/1")

    resp = await http_client.fetch(dashboard_url)
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


@pytest.mark.gen_test
async def test_missing_dashboard(http_client, base_url):
    dashboard_url = urljoin(base_url, "/dashboards/0")

    with pytest.raises(HTTPClientError) as e:
        await http_client.fetch(dashboard_url)

    assert e.value.code == 404


@pytest.mark.gen_test
async def test_create_dashboard(http_client, base_url):
    dashboard_url = urljoin(base_url, "/dashboards")
    payload = {"title": "Test table 5"}
    body = json.dumps(payload)
    request = HTTPRequest(dashboard_url, method="POST", body=body)

    resp = await http_client.fetch(request)
    payload = json.loads(resp.body)

    assert payload["id"]
