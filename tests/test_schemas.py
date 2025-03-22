import json

from faker import Faker
from utils import resource
from app.models.reqres import User, ResponseGetUser
import requests
from jsonschema import validate
from utils.helper import get_user_id

fake = Faker()


def test_user_schema_validate(app_url):
    user = User(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        avatar=fake.image_url(),
    )
    response = requests.post(f"{app_url}/api/users/", json=user._json)
    created_user = response.json()
    schema = json.load(open(resource.path_log_file(file_name='user_schema.json')))
    validate(created_user, schema)

    requests.delete(f"{app_url}/api/users/{created_user["id"]}")



# def test_get_user(app_url, fill_test_data):
#     expected_response_get_user = ResponseGetUser().json
#
#     target_id = get_user_id(app_url)
#     response_2 = requests.get(f"{app_url}/api/users/{target_id}")
#     result_response_get_user = ResponseGetUser(json=response_2.json()).json
#
#     assert result_response_get_user[0]['first_name'] == expected_response_get_user[0]['first_name']


def test_get_user(reqresin, fill_test_data, app_url):
    expected_response_get_user = ResponseGetUser().json
    target_id = get_user_id(reqresin)
    # response = reqresin.get(f"/api/users/{target_id}", verify=False)
    # result_response_get_user = ResponseGetUser(json=response.json()).json

    result_response_get_user = ResponseGetUser(response=reqresin.get(f"/api/users/{target_id}", verify=False)).json

    assert result_response_get_user[0]['first_name'] == expected_response_get_user[0]['first_name']