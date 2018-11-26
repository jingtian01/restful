from flask_restful import Resource, reqparse

from App.apis.UserApi import cache
from App.models import User, db

parser = reqparse.RequestParser()

parser.add_argument('u_icon',type=str)


class AccountResource(Resource):
    #需求  要修改当前数据的active状态
    #方案：通过token获取active 然后修改状态
    def get(self):
        parse = parser.parse_args()
        #获取了参数为token的值
        token = parse.get('u_icon')
        print('-------------------------')
        id = cache.get(token)
        print(id)
        if id:
        # 注意此时users是一个basequery类型的对象 那么获取basequery中的对象的方法是first（）
            users = User.query.filter(User.id.__eq__(id))
            if users.count() > 0:
                user = users.first()
                user.active = True
                db.session.add(user)
                db.session.commit()
                return {'msg': 'i am accoutn'}
        else:
            return {'msg':'i am not account'}
