import uuid

from flask import render_template
from flask_cache import Cache
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import generate_password_hash

from App.ext import mail
from App.models import db, User
cache= Cache(
    config={
        'CACHE_TYPE':'redis',
    }
)
def init_cache(app):
    cache.init_app(app=app)

parser=reqparse.RequestParser()
parser.add_argument(name='u_mail',type=str,required=True,help='邮箱为空，请填写')
parser.add_argument(name='u_password',type=str,required=True,help='密码为空，请填写')

class UserResource(Resource):
    user_fields={
        'id':fields.Integer,
        'u_mail':fields.String,
    }
    result_fields={
        'returncode': fields.String,
        'returnvalue': fields.Nested(user_fields)
    }
    @marshal_with(result_fields)
    def post(self):
        parse=parser.parse_args()
        # name=parse.get('u_name')
        password=parse.get('u_password')
        email=parse.get('u_mail')
        print(email)
        user=User()
        # user.name=name
        password=generate_password_hash(password)
        user.u_password=password
        user.u_mail=email
        print(user.u_mail)
        u_icon=str(uuid.uuid4())
        user.u_icon=u_icon
        print(user.u_icon)

        try:
            print('1233')
            db.session.add(user)
            print('123')
            db.session.commit()
            cache.set(u_icon, user.id, timeout=60)
            print('12345')
            msg=Message(subject='激活',sender='jinfux77@163.com',recipients=[email])
            print(888888)
            html_content=render_template('index.html',email=email,url='127.0.0.1:5000/account/?u_icon=%s'%u_icon)
            print(777)
            msg.html=html_content
            mail.send(msg)
            print('8888')
            return {
                'returncode':'0',
                'returnvalue':user
            }
        except Exception as e:
            return {
                'returncode': '0',
                'returnvalue': str(e)
            }