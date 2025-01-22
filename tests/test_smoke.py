import pytest

import requests
from http import HTTPStatus


def test_status(app_url):
    response = requests.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK


def test_status_users_dates(app_url):
    response = requests.get(f"{app_url}/status")
    result = response.json()
    assert result['users'] == True
