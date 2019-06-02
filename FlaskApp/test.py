from threading import Timer
import time
import psutil
from datetime import datetime

datalist = []
vmdatadata2 = []


def one_process_memo():
    proc = psutil.pids()
    print(type(proc))
    proclist = []
    for a in proc:
        # print(a)
        proclist.append((psutil.Process(a).name(),psutil.Process(a).name()))
    print(proclist)
    return proclist


one_process_memo()
