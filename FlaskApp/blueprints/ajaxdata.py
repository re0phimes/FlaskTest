from flask import Blueprint,render_template, request, flash, current_app, make_response, Response
from jinja2 import Markup
import os, json
from models import ceshi
from pyecharts.charts import Bar, Line, Page
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from models import ceshi, memory, PCmemory
from getPCmemory import getMemory, one_process_memo
from threading import Timer
import getPCmemory
from forms import ProcessForm

ajaxdata_bp = Blueprint('ajaxdata',__name__)


@ajaxdata_bp.route("/process/", methods=['GET'])
def get_process():
    data = one_process_memo()
    process ={}
    process["data"] = data
    return json.dumps(process)