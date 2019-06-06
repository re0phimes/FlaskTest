from flask import Blueprint,render_template, request, flash, current_app, make_response, Response
from jinja2 import Markup
import os, json
from models import ceshi
from pyecharts.charts import Bar, Line, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from models import ceshi, memory, PCmemory
from getPCmemory import getMemory, process_list
from threading import Timer
import getPCmemory
from forms import ProcessForm

ajaxdata_bp = Blueprint('ajaxdata',__name__)


@ajaxdata_bp.route("/process/", methods=['GET'])
def get_process():
    data = process_list()
    process ={}
    process["data"] = data
    return json.dumps(process)


@ajaxdata_bp.route("/testdata/", methods=['GET','POST'])
def getdata():
    finaldata ={}
    finaldata["data"]=getPCmemory.vmdatadata2
    return json.dumps(finaldata)