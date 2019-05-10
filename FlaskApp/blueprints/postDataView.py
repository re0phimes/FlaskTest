from flask import Blueprint,render_template, request, flash
from forms import QueryForm,DBForm
import pandas as pd
from models import PC_memory

postdata_bp = Blueprint('memo', __name__)


@postdata_bp.route("/postdata/", method=['GET','POST']):
def showdata():
    return render_template('getflash.html')
