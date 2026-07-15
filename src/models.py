from datetime import datetime, timezone

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from src import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # nunca guardamos a senha em texto puro, só o hash
    password_hash = db.Column(db.String(255), nullable=False)
    # se o usuário for excluído, suas tarefas vão junto (cascade)
    tasks = db.relationship("Task", backref="owner", lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    # únicos valores aceitos para status e prioridade; a validação de
    # entrada nas rotas usa essas tuplas para rejeitar valores fora daqui
    STATUSES = ("a_fazer", "em_progresso", "concluido")
    PRIORITIES = ("baixa", "media", "alta", "critica")

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.String(500), nullable=True, default="")
    status = db.Column(db.String(20), nullable=False, default="a_fazer")
    priority = db.Column(db.String(20), nullable=False, default="media")
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
        }
