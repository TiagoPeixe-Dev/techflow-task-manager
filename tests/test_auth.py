from tests.conftest import login, register


def test_register_creates_user(client):
    response = register(client)
    assert response.status_code == 200
    assert "Faça login".encode("utf-8") in response.data or b"login" in response.data.lower()


def test_register_rejects_empty_username(client):
    response = client.post(
        "/register", data={"username": "", "password": "senha123"}, follow_redirects=True
    )
    assert b"obrigat\xc3\xb3rios" in response.data


def test_register_rejects_duplicate_username(client):
    register(client)
    response = register(client)
    assert "já existe".encode("utf-8") in response.data


def test_login_succeeds_with_correct_credentials(client):
    register(client)
    response = login(client)
    assert b"Minhas Tarefas" in response.data


def test_login_fails_with_wrong_password(client):
    register(client)
    response = login(client, password="senha_errada")
    assert "inválidos".encode("utf-8") in response.data


def test_tasks_page_requires_login(client):
    response = client.get("/", follow_redirects=True)
    assert b"Entrar" in response.data


def test_logout_redirects_to_login(client):
    register(client)
    login(client)
    response = client.get("/logout", follow_redirects=True)
    assert b"Entrar" in response.data
