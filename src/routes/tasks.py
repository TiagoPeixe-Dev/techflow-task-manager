from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from src import db
from src.models import Task

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/")
@login_required
def list_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.created_at.desc()).all()
    return render_template("tasks.html", tasks=tasks, statuses=Task.STATUSES)


@tasks_bp.route("/tasks", methods=["POST"])
@login_required
def create_task():
    title = request.form.get("title", "").strip()

    if not title:
        flash("O título da tarefa é obrigatório.")
        return redirect(url_for("tasks.list_tasks"))

    task = Task(
        title=title,
        description=request.form.get("description", "").strip(),
        status="a_fazer",
        user_id=current_user.id,
    )
    db.session.add(task)
    db.session.commit()
    return redirect(url_for("tasks.list_tasks"))


def _get_owned_task_or_404(task_id):
    task = db.session.get(Task, task_id)
    if task is None or task.user_id != current_user.id:
        abort(404)
    return task


@tasks_bp.route("/tasks/<int:task_id>/update", methods=["POST"])
@login_required
def update_task(task_id):
    task = _get_owned_task_or_404(task_id)

    status = request.form.get("status")
    if status not in Task.STATUSES:
        flash("Status inválido.")
        return redirect(url_for("tasks.list_tasks"))

    task.status = status
    db.session.commit()
    return redirect(url_for("tasks.list_tasks"))


@tasks_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
@login_required
def delete_task(task_id):
    task = _get_owned_task_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("tasks.list_tasks"))
