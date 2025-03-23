from app.models.reqres import Reqres


def get_user_id_with_model(env) -> int:
    response = Reqres(env).get_users()
    users = response.json()
    target_user = "Janet"
    target_id = None
    for user in users['items']:
        if user['first_name'] == target_user:
            target_id = user['id']
            break
    return target_id
