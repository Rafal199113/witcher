
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
from sqlalchemy import Column, String, Integer, Text,JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session
from addBeastForm import registerBeast


from sql import Glo, sessions


def addGlo(result):
    x=Glo()
    x.name=result['name']
    info=result['info'].split("/")
    char=result['charakter'].split("/")
    look=result['look'].split("/")
    x.info=info
    x.charakter=char
    x.look=look
 
    x.image=result['image']
    sessions.add(x)
    sessions.commit()

def getGlo():
   GetAll = sessions.query(Glo).all()
 
   return GetAll
