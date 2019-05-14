from flask import Blueprint,render_template, request, flash, current_app
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from models import ceshi, memory



postdata_bp = Blueprint('tableviews',__name__)


@postdata_bp.route("/queryData/", methods=['POST','GET'])
def queryData():

#         DBType = request.form.get('DBType',type=str,default=None)
#         username = request.form.get('username', type=str, default=None)
#         password = request.form.get('password', type=str, default=None)
#         host = request.form.get('host', type=str, default=None)
#         DBname = request.form.get('DBname', type=str, default=None)
        Table = request.form.get('Table', type=str, default=None)
        #########
#         current_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','{DBType}+pymysql://{username}:{password}@{host}/{DBname}'.format(DBType=DBType,username=username,password=password,host=host,DBname=DBname))
        ##############
#         tableName = eval(Table)
        if Table != None:
            a = ceshi.query.all()

            page=request.args.get('page',1,type=int)
            taskpagenation = ceshi.query.order_by(ceshi.ID.desc()).paginate(page,per_page=4,error_out=False)
            queryItems = taskpagenation.items
            print(queryItems)
            for line in a:
                keyDict = line.__dict__.keys()
                columnNameList = list(keyDict)[1:]
            return render_template("tableviews/tableOnly.html", a=a, columnNameList=columnNameList,queryItems=queryItems,taskpagenation=taskpagenation)
        else:
            tableName = eval('memory')
            a = tableName.query.all()

            page = request.args.get('page', 1, type=int)
            taskpagenation = tableName.query.order_by(tableName.id.asc()).paginate(page, per_page=4, error_out=False)
            queryItems = taskpagenation.items
            print(queryItems)
            for line in a:
                keyDict = line.__dict__.keys()
                columnNameList = list(keyDict)[1:]
            return render_template("tableviews/tableOnly.html", a=a, columnNameList=columnNameList, queryItems=queryItems,
                                   taskpagenation=taskpagenation)