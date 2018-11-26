
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session

# from App.apis.UserApi import cache
from App.models import db

mail=Mail()

def init_ext(app):
    Session(app=app)
    db.init_app(app=app)
    migrate=Migrate(app=app)
    migrate.init_app(app=app,db=db)
    mail.init_app(app=app)
