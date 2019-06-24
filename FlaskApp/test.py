from threading import Timer
import time, schedule
import psutil
from datetime import datetime
from forms import ProcessForm
from getPCmemory import get_one_process


processDataList = []

def process_list():
    procs = psutil.pids()
    proclist = []
    for aPid in procs:	
        # print(a)
        aProcName = psutil.Process(aPid).name()
        proc_data = (aPid, aProcName)
        proclist.append(proc_data)
    return proclist


def get_one_process(proc_name):
    try:
        global processDataList
        # print(proc_name)
        # proclist = process_list()
        oneProcData = {}
        current_process =  psutil.pids()
        if int(proc_name) in current_process:
            dtime = datetime.now().strftime("%H:%M:%S")  # 只有时分秒
            oneProcData["datetime"] = dtime
            oneProcData["cpu_percent"] = psutil.Process(int(proc_name)).cpu_percent()
            oneProcData["memo_used"] = round(psutil.Process(int(proc_name)).memory_info().rss/1024/1024,2)
            oneProcData["memo_percent"] = round(psutil.Process(int(proc_name)).memory_percent()/1024/1024,2)
            if len(processDataList) < 10:
                processDataList.append(oneProcData)
            else:
                processDataList = processDataList[1:]
                processDataList.append(oneProcData)
            print(processDataList)
        else:
            print("no such process")
    except Exception as e:
        print(e)
        print("eror in get_one_process")



def test_func():
	schedule.every(1).seconds.do(get_one_process,6700)
	while True:
		schedule.run_pending()


test_func()