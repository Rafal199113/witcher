from sqlalchemy import false
from sqlalchemy import create_engine
engine = create_engine('sqlite:///users.db', echo = True)

class user():
    def __init__(self, username, password, islogged ):
        self.username=username
        self.password=password
        self.islogged=islogged
    username=""
    password=""
    islogged=bool(false)
   
