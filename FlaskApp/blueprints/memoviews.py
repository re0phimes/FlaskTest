from flask import Blueprint,render_template, request
from FlaskApp.forms import QueryForm,DBForm
import pandas as pd
from FlaskApp.models import PC_memory

memoview_bp = Blueprint('memo',__name__)

content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
for header in headers:
    print(header)
count = content.count()[0]


@memoview_bp.route('/')
def index():
    page=request.args.get('page',1,type=int)
    pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
    form = QueryForm()
    dbform = DBForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("index.html", headers=headers, count=count, content=content, form=form, pc_memo_data=pc_memo_data, dbform=dbform)
