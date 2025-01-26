import requests
from http import HTTPStatus


# Тест на post: создание. Предусловия: подготовленные тестовые данные

def test_create_user(app_url, new_user):
    data = new_user
    response = requests.post(f"{app_url}/api/users/", json=data)
    created_user = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert created_user['email'] == new_user['email']
    assert created_user['first_name'] == new_user['first_name']
