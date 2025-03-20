import json
from faker import Faker
from utils import resource
from app.models.reqres import User, ResponseGetUser
import requests
from jsonschema import validate

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



def test_get_user(app_url, fill_test_data):
    expected_response_get_user = ResponseGetUser().json
    response = requests.get(f"{app_url}/api/users/")
    users = response.json()
    target_user = "Janet"
    target_id = None
    for user in users['items']:
        if user['first_name'] == target_user:
            target_id = user['id']
            break
    response_2 = requests.get(f"{app_url}/api/users/{target_id}")
    result_response_get_user = ResponseGetUser(json=response_2.json()).json

    assert result_response_get_user[0]['first_name'] == expected_response_get_user[0]['first_name']
