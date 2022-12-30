from ast import increment_lineno
from audioop import add
from cgitb import text
import email
import imp
import json
from os import scandir
from re import S
import sqlite3

from click import echo
from sqlalchemy import Float, MetaData, create_engine
from sqlalchemy import Column, String, Integer, Text,JSON,Table,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from addBeastForm import registerBeast




Base = declarative_base()
conn = sqlite3.connect(":users:.db'")
c = conn.cursor()
class Userr(Base):
    __tablename__ = "user"
    id=Column('id',Integer, primary_key=True, increment_lineno=True)
    username=Column('username',String)
    password=Column('password',String)
    age=Column('age',Integer)
    mail=Column('email',String)
    wallet=Column('wallet', Float)
    enter=Column('enter',Integer)
    def __repr__(self):
        return '<User %r>' % self.username
class Beast(Base):
    __tablename__ = "Bestiariusz"
    id=Column('id',Integer, primary_key=True, increment_lineno=True)
    name=Column('name',String)
    weeknes=Column('weeknes',JSON)
    drop=Column('drop',JSON)
    info=Column('info',Text)
    image=Column('image',String)
  
    def __repr__(self):
        return '<Beast %r>' % self.name
class Glo(Base):
    __tablename__ = "Glosariusz"
    id=Column('id',Integer, primary_key=True, increment_lineno=True)
    name=Column('name',String)
    info=Column('info',JSON)
    charakter=Column('charakter',JSON)
    look=Column('look',JSON)
    image=Column('image',String)
    def __repr__(self):
        return '<Glo %r>' % self.name
class News(Base):
    __tablename__ = "News"
    id=Column('id',Integer, primary_key=True, increment_lineno=True)
    name=Column('name',String)
    info=Column('info',JSON)
    image=Column('image',String)
  
    def __repr__(self):
        return '<News %r>' % self.name
engine = create_engine('sqlite:///:users:.db', echo=True)
conn=engine.connect()
Session = sessionmaker(bind=engine)
sessions=Session()
sessions = scoped_session(sessionmaker(bind=engine))
Base.metadata.create_all(engine)
def create():
 Base.metadata.create_all(engine)
 return 0

def add(login, password, age, email):
 
  user =Userr()
 
  user.username=login
  user.password=password
  user.age=age
  user.mail=email
  user.wallet=0
  sessions.add(user)
  
  sessions.commit()
  sessions.close()

    
def get(login):
 
  oldUser = sessions.query(Userr).filter(Userr.username==login).first()
  
  if oldUser==None:
    return "brak"
  else:
   user = Userr()
   user.username=oldUser.username
   user.password=oldUser.password
   user.mail=oldUser.mail
   user.age=oldUser.age
   print(user.password)
   user.wallet=0
  
   return user
def updateData(user,loggeduser):
  user = sessions.query(Userr).filter(Userr.username==user.username).first()
  user.age=loggeduser['age']
  user.username=loggeduser['username']
  user.mail=loggeduser['email']
  user.password=loggeduser['password1']
  sessions.commit()

def getBeasts():
   beasts = sessions.query(Beast).all()
  
   return beasts

def dodajBeast(id):
  
  x= Beast()
  
  x.name=id['name']
  
  myArray = json.dumps(id['weeknes'])
  myArray2=json.dumps(id['drop'])
  arr=id['weeknes'].split(",")
  arr2=id['drop'].split(",")

  
  x.weeknes=arr
  x.drop=arr2
  x.info=id['info']
  x.image=id['image']
  sessions.add(x)
  sessions.commit()
  



def Top3():
   top = sessions.query(Userr).all()
   enters={}
   for x in top:
     enters[x.username]=x.enter
    
   return enters
     
   
def IncrementEnter(login):
  log = sessions.query(Userr).filter(Userr.username==login).first()
  x = log.enter+1
  
  sessions.query(Userr).filter(Userr.username == login).update({Userr.enter:x}, synchronize_session = False)
  sessions.commit()
  return 0
  