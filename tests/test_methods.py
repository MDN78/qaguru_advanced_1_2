import pytest
from http import HTTPStatus
from app.models.reqres import Reqres


# Тест на post: создание. Предусловия: подготовленные тестовые данные
def test_create_user(env, new_user):
    response = Reqres(env).greate_user(new_user)
    created_user = response.json()
    assert response.status_code == HTTPStatus.CREATED
    assert created_user['email'] == new_user['email']
    assert created_user['first_name'] == new_user['first_name']

    Reqres(env).delete_user(created_user['id'])


# Тест на patch: изменение. Предусловия: созданный пользователь
@pytest.mark.usefixtures("create_new_user")
@pytest.mark.parametrize("email", ["updated_email@test.com"])
def test_update_user(env, create_new_user, email):
    updated_user_info = {'email': email}
    res = Reqres(env).update_user(create_new_user, updated_user_info)
    assert res.status_code == HTTPStatus.OK
    assert res.json()['email'] == updated_user_info['email']

    Reqres(env).delete_user(create_new_user)


# Тест на delete: удаление. Предусловия: созданный пользователь
@pytest.mark.usefixtures("create_new_user")
def test_delete_user(env, create_new_user):
    response = Reqres(env).delete_user(create_new_user)
    assert response.status_code == HTTPStatus.OK
    assert response.json()['message'] == 'User deleted'


# Тест на 405 ошибку
def test_create_user_non_allowed_method(env, new_user):
    response = Reqres(env).greate_user_wrong_method(new_user)
    data = response.json()
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED
    assert 'Method Not Allowed' in data['detail']


# Тест отправить модель без поля на создание ошибка 422
def test_create_user_without_data(env):
    new_user = []
    response = Reqres(env).greate_user(new_user)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


# Тест 404 на удаленного пользователя
# @pytest.mark.usefixtures("create_new_user")
def test_get_deleted_user(env, create_new_user):
    response = Reqres(env).delete_user(create_new_user)
    assert response.status_code == HTTPStatus.OK
    response1 = Reqres(env).get_user_for_test(create_new_user)
    assert response1.status_code == HTTPStatus.NOT_FOUND
    assert response1.json()['detail'] == 'User not found'
