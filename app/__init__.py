from flask import Flask

from instance.config import app_config
from .api.v1.views.question_views import myquestions as qnsv1
from .api.v1.views.answer_views import myanswers as ansv1
#from .api.v1.views.user_views import myusers as usrv1

def create_app(config):
    '''function that creates the flask app'''
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(qnsv1)
    app.register_blueprint(ansv1)
    #app.register_blueprint(usrv1)
    app.config.from_pyfile('config.py')
    return app
