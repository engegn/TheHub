from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://thehub:cas0iWur@thehub:3306/hubdb')
Base = declarative_base()

class Error(Base):
    __tablename__ = 'error'
    id = Column(Integer, primary_key=True)
    error_string = Column(String(256), unique=True)

class Info(Base):
    __tablename__ = 'info'
    id = Column(Integer, primary_key=True)
    info_string = Column(String(256), unique=True)

class Devices(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    description = Column(String(256), unique=True)
    serial_port = Column(String(256), unique=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session=Session()