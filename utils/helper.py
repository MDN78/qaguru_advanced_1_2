
def get_user_id(reqresin) -> int:
    response = reqresin.get("/api/users/")
    users = response.json()
    target_user = "Janet"
    target_id = None
    for user in users['items']:
        if user['first_name'] == target_user:
            target_id = user['id']
            break
    return target_id
