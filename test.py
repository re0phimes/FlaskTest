import psutil
from mysql.connector import connect
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库
DB_connect = "mysql+mysqlconnector://root:123456@localhost:3306/test"
engine = create_engine(DB_connect)



memo = psutil.virtual_memory()
memo.free