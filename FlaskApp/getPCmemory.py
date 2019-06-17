import psutil, time
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from threading import Timer



engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
tempSeriesList = []
finalDFList = []
finalDF = pd.DataFrame(data=None,columns=["timeStamp","total","avai","percent","used","free"])
# print(finalDF)
count = 0

cpudic = {}
cpudic["count"] = psutil.cpu_count()
cpudic["freq"] = psutil.cpu_freq()
cpudic["percentage"] = psutil.cpu_percent()


# --------------------------------
dtimelist = []
valuelist = []
vmdatadata2 = []
processDataList = []

class getMemory:

    def __init__(self,timer_interval):
        self.timer_interval = timer_interval

    def record_sql(self):
        global tempSeriesList, finalDFList, count, finalDF
        while True:
            memo = {}
            memo["total"] = str(round(psutil.virtual_memory().total / 1024 / 1024, 3)) + "MB"
            memo["avai"] = str(round(psutil.virtual_memory().available / 1024 / 1024, 3)) + "MB"
            memo["percent"] = str(psutil.virtual_memory().percent) + "%"
            memo["used"] = str(round(psutil.virtual_memory().used / 1024 / 1024, 3)) + "MB"
            memo["free"] = str(round(psutil.virtual_memory().free / 1024 / 1024, 3)) + "MB"
            timeStamp = str(datetime.now().strftime('%Y-%M-%d %H:%m:%S'))

            memoryList = []
            memoryList.append(timeStamp)
            for value in memo.values():
                memoryList.append(value)
            ser = pd.Series(memoryList)
            tempSeriesList.append(ser)
            # 每秒记录一次数据，数据为series，每5秒生成一个dataframe
            if len(tempSeriesList) >= 5:
                tempDF = pd.DataFrame(tempSeriesList)
                tempDF.columns = ["timeStamp", "total", "avai", "percent", "used", "free"]
                #             print(tempDF)
                tempSeriesList = []
                finalDFList.append(tempDF)
                # print(finalDFList)
                count += 1
            time.sleep(1)
            if count == 2:  # 每次DFList添加了新的数据后，count就会加1，也就是说每5秒count加1.当这里count为10时，则会向最终输出的DF进行合并。
                finalDF = finalDF.append(finalDFList, ignore_index=True)
                # print(finalDF)
                finalDFList = []
                finalDF.to_sql('aaaaa', engine)
                # finalDF.to_csv("aaa.csv")
                count = 0



    # def get_memo(self):
    #     vm = psutil.virtual_memory()
    #     onedata = {}
    #     global vmdatadata2
    #     dtime = datetime.now().strftime("%Y-%m-%d %H:%S:%M")
    #     onedata[dtime] = vm.percent
    #     if len(vmdatadata2) < 10:
    #         vmdatadata2.append(onedata)
    #     else:
    #         vmdatadata2=vmdatadata2[1:]
    #         cpudata.append(onedata)
    #     print(vmdatadata2)
    #     global timer
    #     timer=Timer(getmemo.timer_interval,getmemo.get_memo)
    #     timer.start()
    #
    # def timer_func(self):
    #     getmemo = getMemory(1)
    #     timer=Timer(1,getmemo.get_memo)
    #     timer.start()
    #     time.sleep(1)

def get_memo():
    vm = psutil.virtual_memory()
    # global  dtimelist
    # global valuelist
    global vmdatadata2
    onedata = {}
    # dtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 年月日时分秒
    dtime = datetime.now().strftime("%H:%M:%S") #只有时分秒
    onedata["datetime"] = dtime
    onedata["memo_percent"] = vm.percent
    onedata["memo_used"] = round(vm.used/1024/1024,2)
    onedata["memo_free"] = round(vm.free/1024/1024,2)
    onedata["memo_available"] = round(vm.available/1024/1024,2)
    onedata["memo_total"] = round(vm.total/1024/1024,2)
    onedata["cpu_percent"] = str(psutil.cpu_percent())
    if len(vmdatadata2) < 10:
        vmdatadata2.append(onedata)
    else:
        vmdatadata2 = vmdatadata2[1:]
        vmdatadata2.append(onedata)
    # print(vmdatadata2)
    global timer
    timer=Timer(1,get_memo)
    timer.start()

timer = Timer(1,get_memo)
timer.start()
time.sleep(1)
#-----------------------------------下面为单个程序的CPU、内存数据方法--------------
def process_list():
    procs = psutil.pids()
    proclist = []
    for aPid in procs:
        # print(a)
        aProcName = psutil.Process(aPid).name()
        proc_data = (aPid, aProcName)
        proclist.append(proc_data)
    return proclist

"""
获取一个进程的数据
"""
def get_one_process(proc_name):
    try:
        global processDataList
        # print(proc_name)
        oneProcData = {}
        if int(proc_name) in psutil.pids():
            dtime = datetime.now().strftime("%H:%M:%S")  # 只有时分秒
            oneProcData["datetime"] = dtime
            oneProcData["cpu_percent"] = psutil.Process(int(proc_name)).cpu_percent()
            oneProcData["memo_used"] = round(psutil.Process(int(proc_name)).memory_info().rss/1024/1024,2)
            oneProcData["memo_percent"] = psutil.Process(int(proc_name)).memory_percent()
            if len(processDataList) < 10:
                processDataList.append(oneProcData)
            else:
                processDataList = processDataList[1:]
                processDataList.append(oneProcData)
            # print(processDataList)
        else:
            print("no such process")
        global timer2
        timer2 = Timer(1, get_one_process, [proc_name])
        timer2.start()
    except Exception as e:
        print(e)
        print("eror in get_one_process")
    


def timer_switch(proc_name):
    timer2 = Timer(1, get_one_process, [proc_name])
    timer2.start()
    time.sleep(1)

