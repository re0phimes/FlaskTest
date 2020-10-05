from flask import Blueprint,render_template, request
import json

getip_bp = Blueprint('get_ip', __name__)

@getip_bp.route('/getip/',methods=['GET','POST'])
def get_ip():
    ip = request.remote_addr
    request_header = request.headers
    return render_template('get_ip.html', ip=ip, request_header=request_header)


@getip_bp.route("/ip/", methods=['GET','POST'])
def get_process_status():
    ip = request.remote_addr
    request_header = request.headers
    return json.dumps(request_header)