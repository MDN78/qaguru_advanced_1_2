import requests
from http import HTTPStatus


def test_status(app_url):
    response = requests.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK


def test_status_users_dates(app_url):
    response = requests.get(f"{app_url}/status")
    result = response.json()
    assert result['users'] == True


def test_uncorrect_method_post(app_url):
    response = requests.post(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_uncorrect_method_put(app_url):
    response = requests.post(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_uncorrect_method_delete(app_url):
    response = requests.post(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
