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


def test_list_banks_empty_returns_empty_list(client):
    r = client.get("/api/banks")
    assert r.status_code == 200
    assert r.get_json() == []


def test_update_bank_validation(client):
    r = client.post("/api/banks", json={"name": "Alpha", "location": "NYC"})
    bank_id = r.get_json()["id"]

    r = client.put(f"/api/banks/{bank_id}", json={})
    assert r.status_code == 400


#---------------------

def _create_bank_via_api(client, name="Alpha", location="NYC") -> int:
    r = client.post("/api/banks", json={"name": name, "location": location})
    assert r.status_code == 201
    return r.get_json()["id"]


def test_ui_list_page(client):
    r = client.get("/banks/")
    assert r.status_code == 200
    assert b"Banks" in r.data  # title/heading


def test_ui_new_form_page(client):
    r = client.get("/banks/new")
    assert r.status_code == 200
    assert b"name" in r.data.lower()
    assert b"location" in r.data.lower()


def test_ui_create_bank_redirects(client):
    r = client.post("/banks/new", data={"name": "Alpha", "location": "NYC"}, follow_redirects=False)
    assert r.status_code in (302, 303)


def test_ui_detail_page(client):
    bank_id = _create_bank_via_api(client)

    r = client.get(f"/banks/{bank_id}")
    assert r.status_code == 200
    assert b"Alpha" in r.data


def test_ui_edit_form_page(client):
    bank_id = _create_bank_via_api(client)

    r = client.get(f"/banks/{bank_id}/edit")
    assert r.status_code == 200
    # should contain existing values
    assert b"Alpha" in r.data


def test_ui_update_bank_redirects_and_updates(client):
    bank_id = _create_bank_via_api(client)

    r = client.post(
        f"/banks/{bank_id}/edit",
        data={"name": "Alpha Updated", "location": "LA"},
        follow_redirects=False,
    )
    assert r.status_code in (302, 303)

    # verify via API
    r = client.get(f"/api/banks/{bank_id}")
    assert r.status_code == 200
    assert r.get_json()["location"] == "LA"


def test_ui_delete_bank_redirects_and_deletes(client):
    bank_id = _create_bank_via_api(client)

    r = client.post(f"/banks/{bank_id}/delete", follow_redirects=False)
    assert r.status_code in (302, 303)

    r = client.get(f"/api/banks/{bank_id}")
    assert r.status_code == 404
