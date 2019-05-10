from flask import Blueprint,render_template, request, flash
from forms import QueryForm,DBForm
import pandas as pd
from models import PC_memory

memoview_bp = Blueprint('memo',__name__)

content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
for header in headers:
    print(header)
count = content.count()[0]


@memoview_bp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
        # form = QueryForm()
        # dbform = DBForm()
        DBType = request.form.get('DBType',type=str,default=None)
        timedata = request.form.get('st',type=str,default=None)
        #判断数据库类型#
        return str(DBType) + " " + str(timedata)
    else:
        pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
        form = QueryForm()
        dbform = DBForm()
        if form.validate_on_submit():
            return redirect(url_for('memoviews.index'))
        return render_template("memoviews/index.html", headers=headers, count=count, content=content, form=form, pc_memo_data=pc_memo_data, dbform=dbform)
