from flask import Blueprint,render_template, request
import json
from pymongo import MongoClient
from datetime import datetime


# setup db
myclient = MongoClient('180.76.153.244', 27890)
myclient.admin.authenticate('beihai','yaoduoxiang')
mydb = myclient['proxy_test']
mycol = mydb['requests_recored']

getip_bp = Blueprint('get_ip', __name__)

@getip_bp.route('/getip/',methods=['GET','POST'])
def get_ip():
    ip = request.remote_addr
    request_header = request.headers
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request_list = []
    for x in request_header.values():
        # print(x)
        request_list.append(x)
    data = {"ip":ip, 'datetime':timestamp, "request_header":request_list}
    res = mycol.insert_one(data)
    return render_template('get_ip.html', ip=ip, request_header=request_header)


@getip_bp.route("/ip/", methods=['GET','POST'])
def get_process_status():
    ip = request.remote_addr
    request_header = request.headers
    request_list = []
    for x in request_header.values():
        # print(x)
        request_list.append(x)
    data = {"ip":ip,"request_header":request_list}
    res = mycol.insert_one(data)
    return ip