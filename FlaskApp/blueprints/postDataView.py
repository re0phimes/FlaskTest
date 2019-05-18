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
from models import ceshi, memory, PCmemory



postdata_bp = Blueprint('tableviews',__name__)


@postdata_bp.route("/queryData/", methods=['POST','GET'])
def queryData():

        a = PCmemory.query.all()
        
        page=request.args.get('page',1,type=int)
        taskpagenation = PCmemory.query.order_by(PCmemory.index.desc()).paginate(page,per_page=4,error_out=False)
        queryItems = taskpagenation.items
        print(queryItems)
        for line in a:
            keyDict = line.__dict__.keys()
            columnNameList = list(keyDict)[1:]
        return render_template("tableviews/tableOnly.html", a=a, columnNameList=columnNameList,queryItems=queryItems,taskpagenation=taskpagenation)

    
@postdata_bp.route("/charts/", methods=['POST','GET'])
def visulizeData():
    a = PCmemory.query.all()
    columnNameList = []
    page=request.args.get('page',1,type=int)
    taskpagenation = PCmemory.query.order_by(PCmemory.index.desc()).paginate(page,per_page=10,error_out=False)
    queryItems = taskpagenation.items
    v1 = []
    v2 = []
    xaxis=[]
    for line in a:
            keyDict = line.__dict__.keys()
            columnNameList = list(keyDict)[1:]
            v1.append(line.avai)
            v2.append(line.percent)
            xaxis.append(line.timeStamp)
    v11 = []
    v22 = []
    for i in v1:
        i = i.replace("MB","")
        print(i)
        v11.append(i)
    print(v11)
    for i in v2:
        i = i.replace("%","")
        v22.append(i)
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width= "auto",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("第一条",v11)
        .add_yaxis("第二条",v22)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题")))
    linechart = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width= "auto",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("第一条",v11)
        .add_yaxis("第二条",v22    )
        .set_global_opts(title_opts=opts.TitleOpts(title="linechart", subtitle="onlyfordisplay")))
#     for i in range(len(queryItems)):
#         c.add_yaxis(str(queryItems[i]),queryItems[i])
# 
    return render_template("tableviews/charts.html",c=c.render_embed(),linechart=linechart.render_embed())


