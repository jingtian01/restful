from flask import session
from flask_cache import Cache
from flask_restful import Resource, reqparse, fields, marshal_with
from werkzeug.security import check_password_hash

from App.models import db, Blog, User

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
parser.add_argument(name='b_title',type=str,required=True,help='博客标题为空，请填写')
parser.add_argument(name='b_content',type=str,required=True,help='博客内容为空，请填写')
parser.add_argument(name='modify_b_title',type=str,required=True,help='博客标题为空，请填写')
parser.add_argument(name='modify_b_content',type=str,required=True,help='博客内容为空，请填写')
class Blog_ModifyUserResource(Resource):

    def post(self):
        parse=parser.parse_args()
        name=parse.get('u_mail')
        password=parse.get('u_password')
        session['u_mail']=name
        title = parse.get('b_title')
        content = parse.get('b_content')
        modify_title = parse.get('modify_b_title')
        modify_content = parse.get('modify_b_content')

        users = User.query.filter(User.u_mail.__eq__(name))
        if users.count()>0:
            user=users.first()
            if user:
                if check_password_hash(user.u_password,password):
                    blogs=Blog.query.filter(Blog.b_title.__eq__(title))
                    if blogs.count()>0:
                        blog=blogs.first()
                        db.session.delete(blog)
                        db.session.commit()
                        blog = Blog()
                        blog.b_title=modify_title
                        blog.b_content=modify_content
                        db.session.add(blog)
                        db.session.commit()
                        return {
                            'msg':'登录成功',
                            'msg1': '博客修改成功',
                        }
                    else:
                        return {
                            'msg':'sorry呀，没有这个博客'
                        }
                else:
                    return{'msg':'密码错误'}
            else:
                return {'msg':'用户名不存在'}
        return {'msg':'最后的返回'}





