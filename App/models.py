from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    u_mail = db.Column(db.String(16))
    u_password = db.Column(db.Integer, default=1)
    u_icon = db.Column(db.Integer, default=1)
    is_delete = db.Column(db.Integer, default=1)

class Blog(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    b_title = db.Column(db.String(256))
    b_content = db.Column(db.String(256))


class Collect(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    u_id = db.Column(db.Integer, db.ForeignKey(User.id))
    b_id = db.Column(db.Integer, db.ForeignKey(Blog.id))