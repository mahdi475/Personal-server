def test_notes_require_login(client):
    assert client.get("/notes").status_code == 401
    assert client.post("/notes", json={"title": "Hi"}).status_code == 401


def test_create_and_list_notes(client, login):
    headers = login()
    response = client.post(
        "/notes", json={"title": "First", "content": "Hello"}, headers=headers
    )
    assert response.status_code == 201

    notes = client.get("/notes", headers=headers).json()
    assert len(notes) == 1
    assert notes[0]["title"] == "First"


def test_update_and_delete_note(client, login):
    headers = login()
    note_id = client.post("/notes", json={"title": "Old"}, headers=headers).json()["id"]

    response = client.put(
        f"/notes/{note_id}", json={"title": "New", "content": "Changed"}, headers=headers
    )
    assert response.json()["title"] == "New"

    assert client.delete(f"/notes/{note_id}", headers=headers).status_code == 204
    assert client.get(f"/notes/{note_id}", headers=headers).status_code == 404


def test_users_cannot_see_each_others_notes(client, login):
    mahdi = login("mahdi")
    alma = login("alma")

    note_id = client.post("/notes", json={"title": "Private"}, headers=mahdi).json()["id"]

    assert client.get("/notes", headers=alma).json() == []
    assert client.get(f"/notes/{note_id}", headers=alma).status_code == 404
    assert client.delete(f"/notes/{note_id}", headers=alma).status_code == 404
