import json

from faker import Faker
from utils import resource
from app.models.reqres import User, ResponseGetUser, Reqres
from jsonschema import validate
from utils.helper import get_user_id_with_model

fake = Faker()


def test_user_schema_validate(reqresin):
    user = User(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        avatar=fake.image_url(),
    )
    response = reqresin.post("/api/users/", json=user._json)
    created_user = response.json()
    schema = json.load(open(resource.path_log_file(file_name='user_schema.json')))
    validate(created_user, schema)

    reqresin.delete(f"/api/users/{created_user["id"]}")


def test_get_user_with_object_model(reqresin, env, fill_test_data):
    expected_response_get_user = ResponseGetUser().json
    target_id = get_user_id_with_model(env)
    result_response_get_user = Reqres(env).get_user(target_id)
    assert result_response_get_user[0]['first_name'] == expected_response_get_user[0]['first_name']
