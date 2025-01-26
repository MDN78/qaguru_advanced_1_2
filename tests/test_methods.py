from http.client import responses

import pytest
import requests
from http import HTTPStatus


# Тест на post: создание. Предусловия: подготовленные тестовые данные
# @pytest.mark.skip
def test_create_user(app_url, new_user):
    response = requests.post(f"{app_url}/api/users/", json=new_user)
    created_user = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert created_user['email'] == new_user['email']
    assert created_user['first_name'] == new_user['first_name']



# def test_update_user(app_url, new_user):
#     responses = requests.post(f"{app_url}/api/users/", json=new_user)
#     user_id = responses.json()['id']
#     updated_user_info = {'email': "updated_email@test.com"}
#     res = requests.patch(f"{app_url}/api/users/{user_id}", json=updated_user_info)
#     print(res.json())

@pytest.mark.usefixtures("create_new_user")
def test_update_user(app_url, new_user, create_new_user):
    updated_user_info = {'email': "updated_email@test.com"}
    res = requests.patch(f"{app_url}/api/users/{create_new_user}", json=updated_user_info)
    print(res.json())
    assert res.json()['email'] == updated_user_info['email']
    assert res.status_code == HTTPStatus.OK