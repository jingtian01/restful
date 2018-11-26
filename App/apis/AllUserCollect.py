import pymysql
from flask_restful import Resource, reqparse

from werkzeug.security import check_password_hash

from App.models import User, Blog, Collect, db

parser=reqparse.RequestParser()
parser.add_argument(name='b_title',type=str,required=True,help='博客标题没有输入')


class AllUserCollectResource(Resource):
    def post(self):
        parse=parser.parse_args()
        title=parse.get('b_title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',database='test', charset='utf8')
        cursor = conn.cursor()
        sql='select id from blog where b_title=%s'%title
        cursor.execute(sql)
        letter1 = cursor.fetchall()
        # print(letter1)
        length = letter1.__len__()
        dict1 = {}
        for i in range(length):
            id2 = letter1[i][0]
            print(id2)
            sql2 = 'select u_id from collect where b_id=%s' % id2
            cursor.execute(sql2)
            letter2 = cursor.fetchall()
            print(letter2)
            if letter2:
                length1=letter2.__len__()
                # print('******')
                # print(letter2)
                # print('*******')
                dict1 = {}
                for i in range(length1):
                    # print(length1)
                    id = letter2[i][0]
                    print(id)
                    if letter2[i][0] != letter2[i - 1][0]:
                        print(id)
                        sql3 = 'select u_mail from user where id=%s' % id
                        cursor.execute(sql3)
                        letter3 = cursor.fetchall()
                        print('****')
                        print(letter3)
                        # dict1[id]=letter3[0]
                        print(dict1)
                        dict1[id]={
                            'id':id,
                            'u_mail':letter3[0][0]
                        }
                    else:
                        sql3 = 'select u_mail from user where id=%s' % id
                        cursor.execute(sql3)
                        letter3 = cursor.fetchall()
                        print('****')
                        print(letter3)
                        # dict1[id]=letter3[0]
                        print(dict1)
                        dict1[id] = {
                            'id': id,
                            'u_mail': letter3[0][0]
                        }



                # title = letter2[0][1]
                # content = letter2[0][2]
                # dict1[i] = {
                #     'id': id,
                #     'title': title,
                #     'content': content
                # }
        return {'收藏此博客的用户详情如下': dict1 or '不好意思呀，没人收藏你'}











