import pytest

from src import create_app, db


@pytest.fixture
def app():
    app = create_app("src.config.TestConfig")
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def register(client, username="tiago", password="senha123"):
    return client.post(
        "/register", data={"username": username, "password": password}, follow_redirects=True
    )


def login(client, username="tiago", password="senha123"):
    return client.post(
        "/login", data={"username": username, "password": password}, follow_redirects=True
    )
