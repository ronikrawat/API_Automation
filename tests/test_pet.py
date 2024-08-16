# tests/test_pet.py

def test_create_pet(session, base_url):
    payload = {
        "id": 1,
        "name": "Doggie",
        "photoUrls": ["string"],
        "status": "available"
    }
    response = session.post(f"{base_url}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Doggie"

def test_get_pet_by_id(session, base_url):
    pet_id = 1
    response = session.get(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 200
    assert response.json()["id"] == pet_id

def test_update_pet(session, base_url):
    payload = {
        "id": 1,
        "name": "Doggie Updated",
        "photoUrls": ["string"],
        "status": "sold"
    }
    response = session.put(f"{base_url}/pet", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "sold"

def test_delete_pet(session, base_url):
    pet_id = 1
    response = session.delete(f"{base_url}/pet/{pet_id}")
    assert response.status_code == 200
