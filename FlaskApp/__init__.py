# from flask import Flask,render_template,request
# from FlaskApp.blueprints.memoviews import memoview_bp
# from FlaskApp.extensions import db,bootstrp
# from FlaskApp.models import PC_memory, InRun_memory
# import os
#
#
# def create_app(config_name=None):
#     if config_name is None:
#         config_name = os.getenv('FLASK_CONFIG','development')
#         app = Flask('FlaskApp')
#         app.config.from_object(config[config_name])
#         register_extensions(app)