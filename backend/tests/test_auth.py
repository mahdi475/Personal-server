def test_register(client):
    response = client.post(
        "/auth/register", json={"username": "mahdi", "password": "supersecret123"}
    )
    assert response.status_code == 201
    body = response.json()
    assert body["username"] == "mahdi"
    assert "password" not in body
    assert "password_hash" not in body


def test_register_same_username_twice(client):
    user = {"username": "mahdi", "password": "supersecret123"}
    client.post("/auth/register", json=user)
    response = client.post("/auth/register", json=user)
    assert response.status_code == 409


def test_register_short_password(client):
    response = client.post("/auth/register", json={"username": "mahdi", "password": "123"})
    assert response.status_code == 422


def test_login_wrong_password(client):
    client.post("/auth/register", json={"username": "mahdi", "password": "supersecret123"})
    response = client.post(
        "/auth/login", data={"username": "mahdi", "password": "wrongpassword"}
    )
    assert response.status_code == 401


def test_me(client, login):
    headers = login()
    response = client.get("/auth/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "mahdi"


def test_fake_token_is_rejected(client):
    response = client.get("/auth/me", headers={"Authorization": "Bearer fake.token.here"})
    assert response.status_code == 401
