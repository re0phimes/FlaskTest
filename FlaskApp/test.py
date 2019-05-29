from threading import Timer
import time
import psutil
from datetime import datetime

datalist = []
vmdatadata2 = []


class getMemo:

    def get_memo(self):
        vm = psutil.virtual_memory()
        cpudata = []
        global vmdatadata2
        if len(cpudata) < 10:
            cpudata.append(psutil.cpu_percent(interval=1))
            vmdatadata2.append(vm.used / 1024 / 1024)
        else:
            cpudata = cpudata[1:]
            cpudata.append(psutil.cpu_percent(interval=1))
        print(vmdatadata2)
        ddd = {}
        ddd["sss"] = cpudata
        ddd["datetime"] = datetime.now().strftime("%Y-%m-%d %H:%S:%M")
        datalist = {"cpu": psutil.cpu_percent(interval=1), "memoused": vm.used, "memoavai": vm.available}
        cpudata = []
        # vmdatadata2 =[]
        global timer
        timer = Timer(getmemo.timer_interval, getmemo.get_memo)
        timer.start()


    def timer_func(self):
        # getmemo = getMemo()
        timer = Timer(1, get_memo)
        timer.start()
        time.sleep(1)


