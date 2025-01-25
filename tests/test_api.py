import json
from http import HTTPStatus

import pytest
import requests
from app.models.User import User


# preconditions - add users to database without users id
# scope="module" - this fixture for this module (page)
@pytest.fixture(scope="module")
def fill_test_data(app_url):
    with open("users.json") as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f"{app_url}/api/users/", json=user)
        api_users.append(response.json())

    user_ids = [user["id"] for user in api_users]

    yield user_ids  # test start here, fixture return user_ids

    # delete created users from database
    for user_id in user_ids:
        requests.delete(f"{app_url}/api/users/{user_id}")


# valid values tests
@pytest.mark.usefixtures("fill_test_data")
def test_users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    users_list = response.json()
    for user in users_list:
        User.model_validate(user)


@pytest.mark.usefixtures("fill_test_data")
def test_users_no_duplicates(users):
    users_list = users["items"] if 'items' in users else []
    users_ids = [user["id"] for user in users_list]
    assert len(users_ids) == len(set(users_ids))


def test_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.get(f"{app_url}/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK
        user = response.json()
        User.model_validate(user)


# invalid values tests
@pytest.mark.parametrize("user_id", [13])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.parametrize("user_id", [-1, 0, 'fast'])
def test_user_invalid_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
