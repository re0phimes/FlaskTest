from flask import Blueprint,render_template
from FlaskApp.forms import QueryForm
import pandas as pd


memoview_bp = Blueprint('memo',__name__)

content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
for header in headers:
    print(header)
count = content.count()[0]


@memoview_bp.route('/')
def index():
    form = QueryForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("index.html", headers=headers, count=count, content=content, form=form)
