from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
import pandas as pd
from flask_nav.elements import *
from forms import QueryForm



app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TESTING'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'test secret key'
Bootstrap(app)
# db = SQLAlchemy(app)




@app.route('/',methods=('GET','POST'))
def index():
    form = QueryForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("index.html", headers=headers, count=count, content=content, form=form)


content = pd.read_csv("FlaskApp/static/aaa.csv", index_col=0)
headers = content.columns
for header in headers:
    print(header)
count = content.count()[0]
# print(content)

if __name__ == "__main__":
    app.run(debug=True)

