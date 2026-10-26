def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Mahdi's Personal Server API is running!"}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "ok"}
