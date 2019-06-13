from flask import Blueprint,render_template, request, flash, current_app, make_response, Response
from jinja2 import Markup
import os, json
from models import ceshi
from pyecharts.charts import Bar, Line, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from models import ceshi, memory, PCmemory
from getPCmemory import getMemory, process_list, timer_switch
from threading import Timer
import getPCmemory
from forms import ProcessForm


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
    procForm = ProcessForm()
    procForm.processName.choices = process_list()
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
    for i in v1:
        i = i.replace("MB","")
        # print(i)
        v11.append(i)
    # print(v11)
    for i in v2:
        i = i.replace("%","")
        v22.append(i)
    barchart = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,width= "",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("memo_used",v11,color="dark")
        .add_yaxis("memo_available", v22,color="dark")
        # .add_yaxis("memory percent", v11,yaxis_index=1)
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=20, min_=0, max_=100
            )
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="内存柱形图", subtitle="使用、未使用"),legend_opts=opts.LegendOpts(type_="plain"),yaxis_opts=opts.AxisOpts(type_="value",name_location="end"))
        .set_series_opts(label_opts=opts.LabelOpts(position="insideTopLeft")));

    linechart = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,width= "auto",height= "300px"))
        .add_xaxis(xaxis)
        .add_yaxis("memory percent",v11)
        .add_yaxis("cpu percent",v11)
        .set_global_opts(title_opts=opts.TitleOpts(title="CPU折线图", subtitle="CPU占用率"),yaxis_opts=opts.AxisOpts(min_=0,max_=100)))
    
    barchart.overlap(linechart)

    return render_template("tableviews/charts.html",barchart=Markup(barchart.render_embed()),linechart=Markup(linechart.render_embed()),linechartid="chart_" + linechart.chart_id, barchartid="chart_" + barchart.chart_id, procForm=procForm)



@postdata_bp.route("/oneProcess/", methods=['POST','GET'])
def getOneProcess():
    procForm = ProcessForm()
    procForm.processName.choices = process_list()
    # make the chart instance-----------------------------------
    barchart2 = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,width= "",height= "300px"))
        .add_xaxis([1,2,3,4,5,6,7,8,9,10])
        .add_yaxis("memo_used",[1,2,3,4,5,6,7,8,9,10],color="dark")
        .add_yaxis("memo_available", [1,2,3,4,5,6,7,8,9,10],color="dark")
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} %"), interval=20, min_=0, max_=100
            )
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="内存柱形图", subtitle="使用、未使用"),legend_opts=opts.LegendOpts(type_="plain"),yaxis_opts=opts.AxisOpts(type_="value",name_location="end"))
        .set_series_opts(label_opts=opts.LabelOpts(position="insideTopLeft")));

    linechart2 = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.WONDERLAND,width= "auto",height= "300px"))
        .add_xaxis([1,2,3,4,5,6,7,8,9,10])
        .add_yaxis("memory percent",[1,2,3,4,5,6,7,8,9,10])
        .add_yaxis("cpu percent",[1,2,3,4,5,6,7,8,9,10])
        .set_global_opts(title_opts=opts.TitleOpts(title="CPU折线图", subtitle="CPU占用率"),yaxis_opts=opts.AxisOpts(min_=0,max_=100)))   
    # barchart2.overlap(linechart2)
    normal_page = make_response(render_template("tableviews/one_proc_chart.html",procForm=procForm,barchart2=Markup(barchart2.render_embed()),barchart2id="chart_" + barchart2.chart_id))
    # different request methods------------------------------------
    if request.method == "GET":
        return normal_page
    if request.method == "POST" and procForm.submit.data:
        procdata = request.form.get('processName',type=str,default='InRun.exe')
        timer_switch(procdata)
        return normal_page
