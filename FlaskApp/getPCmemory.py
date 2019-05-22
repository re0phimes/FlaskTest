import psutil, time, json
import pandas as pd
from datetime import datetime
# import matplotlib.pyplot as plt
from sqlalchemy import create_engine


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

memo = {}
memo["total"] = str(psutil.virtual_memory().total/1024/1024) + "MB"
memo["avai"] = str(psutil.virtual_memory().available/1024/1024) + "MB"
memo["percent"] = str(psutil.virtual_memory().percent) + "%"
memo["used"] = str(psutil.virtual_memory().used/1024/1024) + "MB"
memo["free"] = str(psutil.virtual_memory().free/1024/1024) + "MB"
memoryList = []
for value in memo.values():
    memoryList.append(value)
#     print(value)
# columns=['total','available','percent','used','free']

class getMemory():
    def record_memo(self):
        global tempSeriesList, finalDFList, count, finalDF
        while True:
            memo = {}
            memo["total"] = str(round(psutil.virtual_memory().total / 1024 / 1024, 3)) + "MB"
            memo["avai"] = str(round(psutil.virtual_memory().available / 1024 / 1024, 3)) + "MB"
            memo["percent"] = str(psutil.virtual_memory().percent) + "%"
            memo["used"] = str(round(psutil.virtual_memory().used / 1024 / 1024, 3)) + "MB"
            memo["free"] = str(round(psutil.virtual_memory().free / 1024 / 1024, 3)) + "MB"
            timeStamp = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
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

    def another_memo(self):
        vm = psutil.virtual_memory()
        # listdata = [psutil.cpu_percent(interval=1),vm.used/1024/1024,vm.available/1024/1024]
        listdata = []
        listdata2 = []
        while True:
            if len(listdata) < 10:
                listdata2.append(psutil.cpu_percent(interval=1))
                listdata.append(vm.used/1024/1024)
                time.sleep(1)
            else:
                break;
        ddd = {}
        ddd["sss"] = listdata
        ddd["datetime"] = datetime.now().strftime("%Y-%m-%d %H:%S:%M")
        datalist = {"cpu":psutil.cpu_percent(interval=1),"memoused":vm.used,"memoavai":vm.available}
        listdata = []
        listdata2 =[]
        return json.dumps(ddd,ensure_ascii=False)
        # while True:
        #     print(psutil.cpu_percent(interval=1))
        #     print(vm.used / 1024 / 1024 / 1024)
        #     print(vm.available / 1024 / 1024 / 1024)
        #     time.sleep(0.5)


