from flask import Blueprint,render_template, request, flash,g
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



postdata_bp = Blueprint('tableviews',__name__)


@postdata_bp.route("/queryData/", methods=['POST','GET'])
def queryData():

    eng = create_engine(g.DB_URI)

    Base = declarative_base()

    class User(Base):
        __tablename__ = 'User'
        id = Column(Integer, primary_key=True)
        name = Column(String(32))

    class Memory(Base):
        __tablename__ = 'memory'
        id = Column(Integer, primary_key=True)
        timestamp = Column(DateTime)
        used = Column(String(32))
        free = Column(String(32))
    #
    #
    #
    Session = sessionmaker(bind=eng)
    session = Session()
    # if Table == 'memory':
    a = session.query(Memory).all()
    #     return render_template("tableviewstableOnlymemory.html", a=a)
    # else:
    #     a = session.query(User).all()
    #     return render_template("tableviews/tableOnly.html", a=a)
    return render_template("tableviews/tableOnlymemory.html,a=a")
