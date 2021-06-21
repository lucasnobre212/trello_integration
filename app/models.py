from . import db


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(40), primary_key=True)
    token = db.Column(db.String(255), unique=True)
