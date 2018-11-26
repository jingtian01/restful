from flask import Flask

from App import settings
from App.apis import init_apis
from App.apis.UserApi import init_cache
from App.ext import init_ext


def create_app(env_name):
    app=Flask(__name__)
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    app.config.from_object(settings.env.get(env_name))
    init_ext(app)
    init_apis(app)
    init_cache(app)
    return app


