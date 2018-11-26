from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash

from App.models import User, db

parser=reqparse.RequestParser()
parser.add_argument(name='u_mail',type=str,required=True,help='用户名没有输入')
parser.add_argument(name='u_password',type=str,required=True,help='密码没有输入')


class DeleteResource(Resource):
    def delete(self):
        parse=parser.parse_args()
        name=parse.get('u_mail')
        password=parse.get('u_password')
        users = User.query.filter(User.u_mail.__eq__(name))
        if users.count()>0:
            user=users.first()
            if user:
                if check_password_hash(user.u_password,password):
                    db.session.delete(user)
                    db.session.commit()
                    return {'msg':'用户您好，删除成功'}
                else:
                    return{'msg':'密码错误'}
            else:
                return {'msg':'用户名不存在'}
        return {'msg':'最后的返回'}



