from flask import Blueprint,render_template, request, flash, current_app
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from jinja2 import Markup
import os
from models import ceshi
from pyecharts.charts import Bar, Line, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType



postdata_bp = Blueprint('tableviews',__name__)


@postdata_bp.route("/queryData/", methods=['POST','GET'])
def queryData():

#         DBType = request.form.get('DBType',type=str,default=None)
#         username = request.form.get('username', type=str, default=None)
#         password = request.form.get('password', type=str, default=None)
#         host = request.form.get('host', type=str, default=None)
#         DBname = request.form.get('DBname', type=str, default=None)
#         Table = request.form.get('Table', type=str, default=None)
        #########
#         current_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','{DBType}+pymysql://{username}:{password}@{host}/{DBname}'.format(DBType=DBType,username=username,password=password,host=host,DBname=DBname))
        ##############
#         tableName = eval(Table)
        a = ceshi.query.all()
        
        page=request.args.get('page',1,type=int)
        taskpagenation = ceshi.query.order_by(ceshi.ID.desc()).paginate(page,per_page=4,error_out=False)
        queryItems = taskpagenation.items
        print(queryItems)
        for line in a:
            keyDict = line.__dict__.keys()
            columnNameList = list(keyDict)[1:]
        return render_template("tableviews/tableOnly.html", a=a, columnNameList=columnNameList,queryItems=queryItems,taskpagenation=taskpagenation)

    
@postdata_bp.route("/charts/", methods=['POST','GET'])
def visulizeData():
    a = ceshi.query.all()
    columnNameList = []
    page=request.args.get('page',1,type=int)
    taskpagenation = ceshi.query.order_by(ceshi.ID.desc()).paginate(page,per_page=4,error_out=False)
    queryItems = taskpagenation.items
    v1 = []
    v2 = []
    xaxis=[]
    for line in a:
            keyDict = line.__dict__.keys()
            columnNameList = list(keyDict)[1:]
            v1.append(line.aaaa)
            v2.append(line.bbbb)
            xaxis.append(line.ID)
    print(type(queryItems[0]))
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width= "500px",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("第一条",v1)
        .add_yaxis("第二条",v2)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题")))
    linechart = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width= "500px",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("第一条",v1)
        .add_yaxis("第二条",v2)
        .set_global_opts(title_opts=opts.TitleOpts(title="linechart", subtitle="onlyfordisplay")))
#     for i in range(len(queryItems)):
#         c.add_yaxis(str(queryItems[i]),queryItems[i])
# 
    return render_template("tableviews/charts.html",c=c.render_embed(),linechart=linechart.render_embed())