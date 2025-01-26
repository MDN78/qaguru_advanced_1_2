import pytest
import requests
from http import HTTPStatus


# Тест на post: создание. Предусловия: подготовленные тестовые данные

def test_create_user(app_url, new_user):
    response = requests.post(f"{app_url}/api/users/", json=new_user)
    created_user = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert created_user['email'] == new_user['email']
    assert created_user['first_name'] == new_user['first_name']


# Тест на patch: изменение. Предусловия: созданный пользователь

@pytest.mark.usefixtures("create_new_user")
def test_update_user(app_url, new_user, create_new_user):
    updated_user_info = {'email': "updated_email@test.com"}
    res = requests.patch(f"{app_url}/api/users/{create_new_user}", json=updated_user_info)
    assert res.json()['email'] == updated_user_info['email']
    assert res.status_code == HTTPStatus.OK


# Тест на delete: удаление. Предусловия: созданный пользователь
@pytest.mark.usefixtures("create_new_user")
def test_delete_user(app_url, create_new_user):
    response = requests.delete(f"{app_url}/api/users/{create_new_user}")
    assert response.status_code == HTTPStatus.OK
    assert response.json()['message'] == 'User deleted'
