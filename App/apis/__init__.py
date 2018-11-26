from flask_restful import Api

from App.apis.AccountApi import AccountResource
from App.apis.AllBlogCollect import AllBlogCollectResource
from App.apis.AllUserCollect import AllUserCollectResource
from App.apis.Blog_DeleteApi import Blog_DeleteResource
from App.apis.Blog_ModifyApi import Blog_ModifyUserResource
from App.apis.Blog_UserApi import Blog_UserResource
from App.apis.CollectionBlog import CollectionBlogResource
from App.apis.DeleteApi import DeleteResource
from App.apis.LoginApi import LoginResource
from App.apis.ModifyApi import ModifyResource
from App.apis.UserApi import UserResource

api=Api()
#api的初始化要和init联系
def init_apis(app):
    api.init_app(app=app)



api.add_resource(UserResource,'/user/')
api.add_resource(LoginResource,'/login/')
api.add_resource(AccountResource,'/account/')
api.add_resource(ModifyResource,'/modify/')
api.add_resource(DeleteResource,'/delete/')
api.add_resource(Blog_UserResource,'/blog_user/')
api.add_resource(Blog_DeleteResource,'/blog_delete/')
api.add_resource(Blog_ModifyUserResource,'/modify_blog/')
api.add_resource(CollectionBlogResource,'/collection_blog/')
api.add_resource(AllBlogCollectResource,'/allcollection_blog/')
api.add_resource(AllUserCollectResource,'/allcollection_user/')


