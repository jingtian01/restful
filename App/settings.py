def get_database_uri(DATABASE):
    dialect=DATABASE.get('dialect') or 'mysql'
    mysql=DATABASE.get('mysql') or 'pymysql'
    username=DATABASE.get('username') or 'root'
    password=DATABASE.get('password') or 'root'
    host=DATABASE.get('host') or '127.0.0.1'
    port=DATABASE.get('port') or '3306'
    db=DATABASE.get('db') or 'test'
    return '{}+{}://{}:{}@{}:{}/{}'.format(dialect,mysql,username,password,host,port,db)

class Config():
    TEST=True
    DEBUG=False
    SECRET_KEY='111'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SESSION_TYPE ='redis'
    SECRET_KEY = '123'


class DevelopConfig(Config):
    DEBUG = True
    MAIL_SERVER='smtp.163.com'
    MAIL_USERNAME='jinfux77@163.com'
    MAIL_PASSWORD='liu193028'
    DATABASE={
        'dialect':'mysql',
        'mysql':'pymysql',
        'username':'root',
        'password':'root',
        'host':'127.0.0.1',
        'port':'3306',
        'db':'test',
    }
    SQLALCHEMY_DATABASE_URI=get_database_uri(DATABASE)
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True

env={
    'develop':DevelopConfig
}
