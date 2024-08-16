# tests/test_user.py

def test_create_user(session, base_url):
    payload = {
        "id": 1,
        "username": "testuser",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = session.post(f"{base_url}/user", json=payload)
    assert response.status_code == 200

def test_get_user_by_username(session, base_url):
    username = "testuser"
    response = session.get(f"{base_url}/user/{username}")
    assert response.status_code == 200
    assert response.json()["username"] == username

def test_update_user(session, base_url):
    username = "testuser"
    payload = {
        "id": 1,
        "username": "testuser",
        "firstName": "Test Updated",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "newpassword",
        "phone": "0987654321",
        "userStatus": 1
    }
    response = session.put(f"{base_url}/user/{username}", json=payload)
    assert response.status_code == 200

def test_delete_user(session, base_url):
    username = "testuser"
    response = session.delete(f"{base_url}/user/{username}")
    assert response.status_code == 200
