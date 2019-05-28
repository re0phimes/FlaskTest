from threading import Timer
import time
import psutil
from datetime import datetime

datalist = []


def fun_timer():
    global datalist
    vm = psutil.virtual_memory()
    vmdata = {}
    onedata = {}
    vmdata['total'] = vm.total
    vmdata['avai'] = vm.available
    vmdata['used'] = vm.used
    vmdata['free'] = vm.free
    onedata[datetime.now().strftime("%Y-%M-%d %H:%m:%S")] = vmdata
    if len(datalist) < 10:
        datalist.append(onedata)
    else:
        datalist = datalist[1:]
        datalist.append(onedata)
    #     print(a)
    print(datalist)
    global timer
    timer = Timer(1, fun_timer)
    timer.start()


timer = Timer(1, fun_timer)
timer.start()
time.sleep(1)