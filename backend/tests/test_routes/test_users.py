import json

# Each test starts with test_
def test_create_user(client):
    data = {
        "username": "testusername",
        "email": "abc@test.com",
        "password": "1234556"
    }

    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "abc@test.com"
    assert response.json()["username"] == "testusername"