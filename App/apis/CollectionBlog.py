import pymysql
from flask_restful import Resource, reqparse

from werkzeug.security import check_password_hash

from App.models import User, Blog, Collect, db

parser=reqparse.RequestParser()
parser.add_argument(name='u_mail',type=str,required=True,help='用户名没有输入')
parser.add_argument(name='u_password',type=str,required=True,help='密码没有输入')
parser.add_argument(name='b_title',type=str,required=True,help='博客标题没有输入')


class CollectionBlogResource(Resource):
    def post(self):
        parse=parser.parse_args()
        name=parse.get('u_mail')
        password=parse.get('u_password')
        title=parse.get('b_title')
        users = User.query.filter(User.u_mail.__eq__(name))
        print('11')
        if users.count()>0:
            print('22')
            user=users.first()
            if user:
                id1=user.id
                if check_password_hash(user.u_password,password):
                    blogs = Blog.query.filter(Blog.b_title.__eq__(title))
                    print(blogs.count())
                    if blogs.count()>0:
                        blog=blogs.first()
                        if blog:
                            print(blog)
                            conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',database='test', charset='utf8')
                            cursor = conn.cursor()
                            sql='select id from blog where b_title=%s'%title
                            cursor.execute(sql)
                            letter1 = cursor.fetchone()
                            id2=letter1[0]
                            collect=Collect()
                            collect.b_id=id2
                            collect.u_id=id1
                            db.session.add(collect)
                            db.session.commit()
                            return {
                                'msg':'博客收藏成功，您收藏的博客标题是：%s'%title
                            }
                        else:
                            return {
                                'msg':'出错啦，'
                            }
                    else:
                        return {
                            'msg':''
                        }
                else:
                    return{'msg':'密码错误'}
            else:
                return {'msg':'用户名不存在'}
        return {'msg':'搜索不到该用户哦'}








