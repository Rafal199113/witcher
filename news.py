
from audioop import add
from cgitb import text
import email
import imp
import json
from os import scandir
from re import S, X
import sqlite3

from click import echo
from sqlalchemy import Float, MetaData, create_engine
from sqlalchemy import Column, String, Integer, Text,JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from addBeastForm import registerBeast


from sql import sessions, News

def addNews(result2):
    c=News()

    c.name=result2['name']
    info=result2['info'].split("/")
    c.info=info
    c.image=result2['image']
    sessions.add(c)
    sessions.commit()
def getNews():
   news = sessions.query(News).all()
 
   return news

def delNews(id):
     dell = sessions.query(News).filter(News.id==id).first()
     sessions.delete(dell)
     sessions.commit()
     return 0

    
    
 

    