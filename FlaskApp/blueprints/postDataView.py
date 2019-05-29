from flask import Blueprint,render_template, request, flash, current_app
from jinja2 import Markup
import os, json
from models import ceshi
from pyecharts.charts import Bar, Line, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from models import ceshi, memory, PCmemory
from getPCmemory import getMemory
from getPCmemory import vmdatadata2

postdata_bp = Blueprint('tableviews',__name__)


@postdata_bp.route("/queryData/", methods=['POST','GET'])
def queryData():

        a = PCmemory.query.all()
        
        page=request.args.get('page',1,type=int)
        taskpagenation = PCmemory.query.order_by(PCmemory.index.desc()).paginate(page,per_page=4,error_out=False)
        queryItems = taskpagenation.items
        # print(queryItems)
        for line in a:
            keyDict = line.__dict__.keys()
            columnNameList = list(keyDict)[1:]
        return render_template("tableviews/tableOnly.html", a=a, columnNameList=columnNameList,queryItems=queryItems,taskpagenation=taskpagenation)

    
@postdata_bp.route("/charts/", methods=['POST','GET'])
def visulizeData():
    a = PCmemory.query.all()
    # columnNameList = []
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
    print(v11)
    for i in v1:
        i = i.replace("MB","")
        # print(i)
        v11.append(i)
    # print(v11)
    for i in v2:
        i = i.replace("%","")
        v22.append(i)
    barchart = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WESTEROS,width= "",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("第一条",v11)
        .add_yaxis("第二条",v22)
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题")))
    linechart = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width= "auto",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("第一条",v11)
        .add_yaxis("第二条",v22)
        .set_global_opts(title_opts=opts.TitleOpts(title="linechart", subtitle="onlyfordisplay")))
    return render_template("tableviews/charts.html",barchart=Markup(barchart.render_embed()),linechart=Markup(linechart.render_embed()),linechartid="chart_" + linechart.chart_id, barchartid="chart_" + barchart.chart_id)


@postdata_bp.route("/testdata/", methods=['GET'])
def getdata():
    getvmdata = getMemory(1)
    getvmdata.timer_func()
    return json.dumps(vmdatadata2[0])