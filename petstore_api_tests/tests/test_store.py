# tests/test_store.py

def test_place_order(session, base_url):
    payload = {
        "id": 1,
        "petId": 1,
        "quantity": 1,
        "shipDate": "2024-08-16T15:30:00.000Z",
        "status": "placed",
        "complete": True
    }
    response = session.post(f"{base_url}/store/order", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "placed"

def test_get_order_by_id(session, base_url):
    order_id = 1
    response = session.get(f"{base_url}/store/order/{order_id}")
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_delete_order(session, base_url):
    order_id = 1
    response = session.delete(f"{base_url}/store/order/{order_id}")
    assert response.status_code == 200
