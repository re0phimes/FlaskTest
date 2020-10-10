from flask import Blueprint,render_template, request, flash, get_flashed_messages, Flask, redirect, current_app
# from forms import QueryForm,DBForm
import pandas as pd
# from extensions import db
# from models import User, ceshi, memory #
import os
from pymongo import MongoClient


# content = pd.read_csv("static/aaa.csv", index_col=0)
# headers = content.columns
# # for header in headers:
# #     print(header)
# count = content.count()[0]
memoview_bp = Blueprint('memo',__name__)
myclient = MongoClient('180.76.153.244', 27890)
myclient.admin.authenticate('beihai','yaoduoxiang')
mydb = myclient['proxy_test']
mycol = mydb['requests_recored']



@memoview_bp.route('/',methods=['GET','POST'])
def index():
    ip = request.remote_addr
    request_header = request.headers
    request_list = []
    for x in request_header.values():
        # print(x)
        request_list.append(x)
    data = {"ip":ip,"request_header":request_list}
    res = mycol.insert_one(data)
    return render_template('memoviews/index2.html', ip=ip, request_header=request_header)






# def index():
#     if request.method == 'POST':
#         DBType = request.form.get('DBType',type=str,default=None)
#         username = request.form.get('username', type=str, default=None)
#         password = request.form.get('password', type=str, default=None)
#         host = request.form.get('host', type=str, default='localhost')
#         DBname = request.form.get('DBname', type=str, default=None)
#         Table = request.form.get('Table', type=str, default=None)
#         #########
# #         current_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','{DBType}+mysqlconnector://{username}:{password}@{host}/{DBname}'.format(DBType=DBType,username=username,password=password,host=host,DBname=DBname))
#         current_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','{DBType}+mysqlconnector://{username}:{password}@{host}/{DBname}'.format(DBType=DBType,username=username,password=password,host=host,DBname=DBname))
# #         ##############
# #         tableName = eval(Table)
# #         a = tableName.query.all()
#
# #         page=request.args.get('page',1,type=int)
# #         taskpagenation = tableName.query.order_by(tableName.ID.desc()).paginate(page,per_page=4,error_out=False)
# #         queryItems = taskpagenation.items
# #         print(queryItems)
# #         for line in a:
# #             keyDict = line.__dict__.keys()
# #             columnNameList = list(keyDict)[1:]
# #         return render_template("tableviews/tableOnly.html", a=a, columnNameList=columnNameList,queryItems=queryItems,taskpagenation=taskpagenation)
#         return redirect("/tableviews/queryData/")
#
#     else:
#         # pc_memo_data = PC_memory.query.order_by(PC_memory.timestamp.desc())
#         form = QueryForm()
#         dbform = DBForm()
#         if form.validate_on_submit():
#             return redirect(url_for('memoviews.index'))
#         return render_template("memoviews/index.html", headers=headers, count=count, content=content, form=form, dbform=dbform)
