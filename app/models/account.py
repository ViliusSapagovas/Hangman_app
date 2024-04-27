from app.extensions import db
from flask_login import UserMixin


class Account(db.Model, UserMixin):
    __tablename__ = "accounts"

    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column("username", db.String(20), unique=True, nullable=False)
    name = db.Column("name", db.String(60), nullable=False)
    surname = db.Column("surname", db.String(60), nullable=False)
    password = db.Column("password", db.String(60), nullable=False)
    email = db.Column("email", db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<account "{self.title}">'