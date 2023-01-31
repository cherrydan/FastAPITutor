import json

import pytest


@pytest.mark.asyncio
async def test_create_user(client, get_user_from_database):
    user_data = {
        "name": "Nikolay",
        "surname": "Swiridow",
        "email": "lol@kek.com"
    }
    resp = client.post("/user/", data=json.dumps(user_data))
    data_from_resp = resp.json()
    assert resp.status_code == 200
    assert data_from_resp["name"] == user_data["name"]
    assert data_from_resp["surname"] == user_data["surname"]
    assert data_from_resp["email"] == user_data["email"]
    # users_from_db = get_user_from_database(user_data["user_id"])
    # assert len(users_from_db) == 1
    # user_from_db = dict[users_from_db[0]]
    # assert user_from_db["name"] == user_data["name"]
    # assert user_from_db["surname"] == user_data["surname"]
    # assert user_from_db["email"] == user_data["email"]
    # assert user_from_db["is_activa"] == True
    # assert str(user_from_db["user_id"]) == user_data["user_id"]