from flask import Flask

from instance.config import app_config
from .api.v1.views.views import myapi as apiv1

def create_app(config):
    '''function creating the flask app'''
    app = Flask(__name__)
    app.register_blueprint(apiv1)
    app.config.from_object(app_config[config])
    return app
