from flask import Blueprint,render_template, request, flash, get_flashed_messages, Flask, redirect, current_app
from forms import QueryForm,DBForm
import pandas as pd
from extensions import db
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import g
from models import PC_memory
import os
from flask_sqlalchemy import SQLAlchemy



content = pd.read_csv("static/aaa.csv", index_col=0)
headers = content.columns
# for header in headers:
#     print(header)
count = content.count()[0]
memoview_bp = Blueprint('memo',__name__)

class User(db.Model):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ceshi(db.Model):
    __tablename__ = 'ceshi'
    aaaa = Column(String(32))
    bbbb = Column(String(32))
    ID = Column(Integer, primary_key=True)

    def __init__(self, aaaa, bbbb, ID):
        self.aaaa = aaaa
        self.bbbb = bbbb
        self.ID = ID



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
        Table = request.form.get('Table', type=str, default=None)
        #########
        current_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','{DBType}+mysqlconnector://{username}:{password}@{host}/{DBname}'.format(DBType=DBType,username=username,password=password,host=host,DBname=DBname))
        ##############
        

#         Base = declarative_base()

#         class User(Base):
#             __tablename__ = 'User'
#             id = Column(Integer, primary_key=True)
#             name = Column(String(32))
        
        
        
#         class Memory(Base):
#             __tablename__ = 'memory'
#             id = Column(Integer, primary_key=True)
#             timestamp = Column(DateTime)
#             used = Column(String(32))
#             free = Column(String(32))


#         DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}"
#         g.DB_URI = DB_URI.format(user=username,password=password,host=host,port=3306,db=DBname)
#         eng = create_engine(DB_URI.format(user=username,password=password,host=host,port=3306,db=DBname))

#         Session = sessionmaker(bind=eng)
#         session = Session()

        

        if Table == 'ceshi':
            a = ceshi.query.all()
            for line in a:
                print(line)
                print(type(line))
            return render_template("tableviews/tableOnlymemory.html", a=a)
        else:
            a = User.query.all()
            print(a)
#             a = session.query(User).all()
            return render_template("tableviews/tableOnly.html", a=a)

    else:
        # pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
        form = QueryForm()
        dbform = DBForm()
        if form.validate_on_submit():
            return redirect(url_for('memoviews.index'))
        return render_template("memoviews/index.html", headers=headers, count=count, content=content, form=form, dbform=dbform)