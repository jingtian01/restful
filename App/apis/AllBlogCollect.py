import pymysql
from flask_restful import Resource, reqparse

from werkzeug.security import check_password_hash

from App.models import User, Blog, Collect, db

parser=reqparse.RequestParser()
parser.add_argument(name='u_mail',type=str,required=True,help='用户名没有输入')
parser.add_argument(name='u_password',type=str,required=True,help='密码没有输入')

class AllBlogCollectResource(Resource):
    def post(self):
        parse=parser.parse_args()
        name=parse.get('u_mail')
        password=parse.get('u_password')
        users = User.query.filter(User.u_mail.__eq__(name))
        if users.count()>0:
            user=users.first()
            if user:
                id1=user.id
                if check_password_hash(user.u_password,password):
                    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',database='test', charset='utf8')
                    cursor = conn.cursor()
                    sql='select b_id from collect where u_id=%s'%id1
                    cursor.execute(sql)
                    letter1 = cursor.fetchall()
                    print('1111')
                    length=letter1.__len__()
                    dict1 = {}
                    for i in range(length):
                        id2=letter1[i][0]
                        print(id2)
                        if letter1[i][0]!=letter1[i-1][0]:
                            sql2='select * from blog where id=%s'%id2
                            cursor.execute(sql2)
                            letter2 = cursor.fetchall()
                            print(letter2)
                            id=letter2[0][0]
                            print(id)
                            title=letter2[0][1]
                            content=letter2[0][2]

                            dict1[i]={
                                'id':id,
                                'title':title,
                                'content':content
                            }
                        else:
                            sql2 = 'select * from blog where id=%s' % id2
                            cursor.execute(sql2)
                            letter2 = cursor.fetchall()
                            print(letter2)
                            id = letter2[0][0]
                            print(id)
                            title = letter2[0][1]
                            content = letter2[0][2]

                            dict1[i] = {
                                'id': id,
                                'title': title,
                                'content': content
                            }
                        sql2 = 'select * from blog where id=%s' % id2
                        cursor.execute(sql2)
                        letter2 = cursor.fetchall()
                        print(letter2)
                        id = letter2[0][0]
                        print(id)
                        title = letter2[0][1]
                        content = letter2[0][2]

                        dict1[i] = {
                            'id': id,
                            'title': title,
                            'content': content
                        }

                    print(dict1)

                    return {'用户所收藏的博客详情如下':dict1 or '你还没有收藏博客哦'}

                else:
                    return{'msg':'密码错误'}
            else:
                return {'msg':'用户名不存在'}
        return {'msg':'最后的返回'}








