

from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash, generate_password_hash

from App.models import User, db

parser=reqparse.RequestParser()
parser.add_argument(name='u_mail',type=str,required=True,help='用户名没有输入')
parser.add_argument(name='u_password',type=str,required=True,help='密码没有输入')
parser.add_argument(name='modify_u_password',type=str,required=True)


class ModifyResource(Resource):
    def post(self):
        parse=parser.parse_args()
        name=parse.get('u_mail')
        password=parse.get('u_password')
        re_password=parse.get('modify_u_password')
        re_password=generate_password_hash(re_password)

        users = User.query.filter(User.u_mail.__eq__(name))
        if users.count()>0:
            user=users.first()
            if user:
                if check_password_hash(user.u_password,password):
                    user=users.first()
                    db.session.delete(user)
                    db.session.commit()
                    user=User()
                    user.u_mail=name
                    user.u_password=re_password
                    db.session.add(user)
                    db.session.commit()
                    return {'msg':'您的密码修改成功'}
                else:
                    return{'msg':'密码错误'}
            else:
                return {'msg':'用户名不存在'}
        return {'msg':'最后的返回'}






