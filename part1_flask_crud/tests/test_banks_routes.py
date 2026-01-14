def test_create_and_get_bank(client):
    r = client.post("/api/banks", json={"name": "Alpha", "location": "NYC"})
    assert r.status_code == 201
    bank_id = r.get_json()["id"]

    r = client.get(f"/api/banks/{bank_id}")
    assert r.status_code == 200
    assert r.get_json()["name"] == "Alpha"


def test_list_banks_contains_created(client):
    r = client.post("/api/banks", json={"name": "Alpha", "location": "NYC"})
    bank_id = r.get_json()["id"]

    r = client.get("/api/banks")
    assert r.status_code == 200
    assert any(bank["id"] == bank_id for bank in r.get_json())


def test_update_bank(client):
    r = client.post("/api/banks", json={"name": "Alpha", "location": "NYC"})
    bank_id = r.get_json()["id"]

    r = client.put(f"/api/banks/{bank_id}", json={"name": "Alpha Updated", "location": "LA"})
    assert r.status_code == 200
    assert r.get_json()["location"] == "LA"


def test_delete_bank(client):
    r = client.post("/api/banks", json={"name": "Alpha", "location": "NYC"})
    bank_id = r.get_json()["id"]

    r = client.delete(f"/api/banks/{bank_id}")
    assert r.status_code == 204

    r = client.get(f"/api/banks/{bank_id}")
    assert r.status_code == 404


def test_create_bank_validation(client):
    resp = client.post("/api/banks", json={})
    assert resp.status_code == 400


def test_update_not_found(client):
    resp = client.put("/api/banks/999", json={"name": "Missing", "location": "Nowhere"})
    assert resp.status_code == 404


def test_delete_not_found(client):
    resp = client.delete("/api/banks/999")
    assert resp.status_code == 404


def test_get_not_found(client):
    resp = client.get("/api/banks/999")
    assert resp.status_code == 404
