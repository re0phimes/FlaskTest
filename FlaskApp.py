from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
import pandas as pd
from flask_nav import Nav
from flask_nav.elements import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


class QueryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='name cannot be empty')], render_kw={'placeholder':'Data'})
    st = StringField('StartTime', render_kw={'placeholder':'StartTime'})
    et = StringField('EndTime', render_kw={'placeholder':'EndTime'})
    submit = SubmitField('Go')

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'test secret key'
Bootstrap(app)
db = SQLAlchemy(app)




@app.route('/',methods=('GET','POST'))
def index():
    form = QueryForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("index.html", headers=headers, count=count, content=content, form=form)


content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
for header in headers:
    print(header)
count = content.count()[0]
# print(content)

if __name__ == "__main__":
    app.run(debug=True)

