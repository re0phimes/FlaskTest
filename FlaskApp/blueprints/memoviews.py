from flask import Blueprint,render_template, request, flash, get_flashed_messages, Flask
from forms import QueryForm,DBForm
import pandas as pd
from models import PC_memory
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
# for header in headers:
#     print(header)
count = content.count()[0]
memoview_bp = Blueprint('memo',__name__)

@memoview_bp.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
        # form = QueryForm()
        # dbform = DBForm()
        DBType = request.form.get('DBType',type=str,default=None)
        username = request.form.get('username', type=str, default=None)
        password = request.form.get('password', type=str, default=None)
        host = request.form.get('host', type=str, default=None)
        DBname = request.form.get('DBname', type=str, default=None)
        #########
#         app = Flask(__name__)
#         app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','%s://%s:%s@%s/%s' %(DBType,username,password,host,DBname))
        ######################

        Base = declarative_base()

        class User(Base):
            __tablename__ = 'User'
            id = Column(Integer, primary_key=True)
            name = Column(String(32))
        
        DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
        eng = create_engine(DB_URI.format(user=username,password=password,host=host,port=3306,db=DBname))

        Session = sessionmaker(bind=eng)
        session = Session()
        a = session.query(User).all()
        #判断数据库类型#
        print(type(a))
        for lines in a:
            print(lines)
            print(type(lines))
        return render_template("tableviews/tableOnly.html", a=a)
    else:
        # pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
        form = QueryForm()
        dbform = DBForm()
        if form.validate_on_submit():
            return redirect(url_for('memoviews.index'))
        return render_template("memoviews/index.html", headers=headers, count=count, content=content, form=form, dbform=dbform)