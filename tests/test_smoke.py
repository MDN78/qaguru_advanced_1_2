import os
import socket
import requests
import pytest
from http import HTTPStatus
from app.models.reqres import Reqres


def test_status(env):
    response = Reqres(env).get_status()
    assert response.status_code == HTTPStatus.OK


def test_server_responds_on_port(port):
    local_host = os.getenv("HOST")
    with socket.create_connection((local_host, port)):
        assert True, f"Server should be responding on port {port}."


def test_status_users_dates(env):
    response = Reqres(env).get_status()
    result = response.json()
    assert result['database'] == True


@pytest.mark.parametrize("method", ["post", "put", "delete", "patch"])
def test_status_invalid_methods(app_url, method):
    url = f"{app_url}/status/"
    response = getattr(requests, method)(url)
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
