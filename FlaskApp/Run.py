from flask import Flask, render_template, redirect
from flask_cors import *
from flask_debugtoolbar import DebugToolbarExtension
from extensions import db
from flask_bootstrap import Bootstrap
# from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.jinja_env.auto_reload = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@localhost/test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'test secret key'



CORS(app, resources=r'/*')
# db.init_app(app)
Bootstrap(app)
# toolbar = DebugToolbarExtension(app)




# from blueprints.postDataView import postdata_bp
from blueprints.memoviews import memoview_bp
from blueprints.get_ip import getip_bp
# from blueprints.ajaxdata import ajaxdata_bp

app.register_blueprint(memoview_bp)
app.register_blueprint(getip_bp)
# app.register_blueprint(postdata_bp, url_prefix='/tableviews/')
# app.register_blueprint(ajaxdata_bp, url_prefix='/ajaxdata/')


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000, debug=True)

