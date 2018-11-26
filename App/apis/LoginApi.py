from flask import session
from flask_restful import Resource, reqparse
from flask_session import Session
from werkzeug.security import check_password_hash

from App.models import User

parser=reqparse.RequestParser()
parser.add_argument(name='u_mail',type=str,required=True,help='用户名没有输入')
parser.add_argument(name='u_password',type=str,required=True,help='密码没有输入')


class LoginResource(Resource):
    def post(self):
        parse=parser.parse_args()
        name=parse.get('u_mail')
        password=parse.get('u_password')
        session['u_mail']=name
        users = User.query.filter(User.u_mail.__eq__(name))
        if users.count()>0:
            user=users.first()
            if user:
                if check_password_hash(user.u_password,password):
                        return {'msg':'登陆成功，欢迎来到断剑天涯武侠世界'}
                else:
                    return{'msg':'密码错误'}
            else:
                return {'msg':'用户名不存在'}
        return {'msg':'最后的返回'}



