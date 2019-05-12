from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from extensions import bootstrp, db
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
Bootstrap(app)
db.init_app(app)
toolbar = DebugToolbarExtension(app)

app.jinja_env.auto_reload = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.secret_key = 'test secret key'



from blueprints.memoviews import memoview_bp
app.register_blueprint(memoview_bp, url_prefix='')


if __name__ == "__main__":
    app.run(debug=True)

