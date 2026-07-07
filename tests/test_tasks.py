from src import db
from src.models import Task
from tests.conftest import login, register


def _create_task(client, title="Nova tarefa", description="", priority=None):
    data = {"title": title, "description": description}
    if priority is not None:
        data["priority"] = priority
    return client.post("/tasks", data=data, follow_redirects=True)


def test_create_task_with_valid_title(client, app):
    register(client)
    login(client)
    _create_task(client, title="Configurar repositório")

    with app.app_context():
        tasks = Task.query.all()
        assert len(tasks) == 1
        assert tasks[0].title == "Configurar repositório"
        assert tasks[0].status == "a_fazer"
        assert tasks[0].priority == "media"


def test_create_task_rejects_empty_title(client, app):
    register(client)
    login(client)
    _create_task(client, title="")

    with app.app_context():
        assert Task.query.count() == 0


def test_update_task_status(client, app):
    register(client)
    login(client)
    _create_task(client)

    with app.app_context():
        task = Task.query.first()
        task_id = task.id

    client.post(f"/tasks/{task_id}/update", data={"status": "em_progresso"}, follow_redirects=True)

    with app.app_context():
        assert db.session.get(Task, task_id).status == "em_progresso"


def test_update_task_rejects_invalid_status(client, app):
    register(client)
    login(client)
    _create_task(client)

    with app.app_context():
        task_id = Task.query.first().id

    client.post(
        f"/tasks/{task_id}/update", data={"status": "status_invalido"}, follow_redirects=True
    )

    with app.app_context():
        assert db.session.get(Task, task_id).status == "a_fazer"


def test_delete_task(client, app):
    register(client)
    login(client)
    _create_task(client)

    with app.app_context():
        task_id = Task.query.first().id

    client.post(f"/tasks/{task_id}/delete", follow_redirects=True)

    with app.app_context():
        assert Task.query.count() == 0


def test_user_cannot_access_another_users_task(client, app):
    register(client, username="alice")
    login(client, username="alice")
    _create_task(client, title="Tarefa da Alice")

    with app.app_context():
        task_id = Task.query.first().id

    client.get("/logout", follow_redirects=True)
    register(client, username="bob")
    login(client, username="bob")

    response = client.post(f"/tasks/{task_id}/delete", follow_redirects=True)
    assert response.status_code == 404


def test_create_task_with_valid_priority(client, app):
    register(client)
    login(client)
    _create_task(client, title="Corrigir bug crítico", priority="critica")

    with app.app_context():
        assert Task.query.first().priority == "critica"


def test_create_task_falls_back_to_default_priority_when_invalid(client, app):
    register(client)
    login(client)
    _create_task(client, priority="urgentissima")

    with app.app_context():
        assert Task.query.first().priority == "media"


def test_update_task_priority(client, app):
    register(client)
    login(client)
    _create_task(client)

    with app.app_context():
        task_id = Task.query.first().id

    client.post(f"/tasks/{task_id}/priority", data={"priority": "alta"}, follow_redirects=True)

    with app.app_context():
        assert db.session.get(Task, task_id).priority == "alta"


def test_update_task_rejects_invalid_priority(client, app):
    register(client)
    login(client)
    _create_task(client)

    with app.app_context():
        task_id = Task.query.first().id

    client.post(
        f"/tasks/{task_id}/priority", data={"priority": "invalida"}, follow_redirects=True
    )

    with app.app_context():
        assert db.session.get(Task, task_id).priority == "media"
