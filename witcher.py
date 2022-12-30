from ast import Global
from asyncore import write
from cgitb import reset
from crypt import methods
from distutils.log import Log
from email import message


import os
from unittest import result





from click import edit
from flask_recaptcha import ReCaptcha 
from flask import json, Flask,url_for, redirect, make_response, render_template, send_file, request, send_from_directory,jsonify, session

from sqlalchemy import true

from login import Singup;
from sql import Beast, add, get,updateData,create, getBeasts, dodajBeast,Top3,IncrementEnter
from registerform import register
from login import Singup
from sql import Userr,sessions
from addBeastForm import registerBeast
from addGloForm import  registerGlo
from editform import Edit
from sqlGlo import addGlo,Glo
from sqlGlo import getGlo
from newsForm import News
from news import addNews,getNews,delNews
UPLOAD_DIRECTORY = "static/wallpapers"
from datetime import date, datetime
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)

cycki=Userr()
LogUser=Userr()
app.config['SECRET_KEY']='witcher'
app.config['RECAPTCHA_SITE_KEY'] = '6Le65fAeAAAAAJmugEtxzuib1RmHc-xr_XXG1LtU' 
app.config['RECAPTCHA_SECRET_KEY'] = '6Le65fAeAAAAADa7BpVuthTBsg_wfx8aBzHz-OqR' 
recaptcha = ReCaptcha(app) 

      
         
@app.route("/",methods=['GET','POST'])
def hello_world():
   
   session.pop('login',None)
   print('login' in session)
   if 'login' in session:
      return redirect("/main")
   else:
      return redirect('/loginn')
           

         

   
    
                  
     #kontoller wyświetlający formularz logwania 
@app.route('/change', methods=['GET','POST'])
def change():
  
  if request.method == "POST":
     result = request.form.to_dict()
     vocab = list(result)
     print()
     x= sessions.query(Beast).filter(Beast.id==int(result.get(vocab[0]))).first()
     x.image=vocab[0]
     sessions.commit()
   
     
           
  
     return json.dumps('{"'+vocab[0]+'":"sd"}')
@app.route('/loginn', methods=['GET','POST'])   
def loginn():
   loginform= Singup()
   session.pop('login',None)
   
   if request.method == 'POST':
      if loginform.is_submitted():
            result=request.form  
            
       
           
            
            
            if get(result['username'])!="brak":
               global LogUser
               LogUser=get(result['username'])
               session['login'] = LogUser.username
               IncrementEnter(LogUser.username)
               now = datetime.now() 
               date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
             
               resp = make_response(redirect("/main"))
               resp.set_cookie(LogUser.username, date_time)
               return resp
                
            else:   return render_template('singup.html',  form=loginform, message="Brak takiego użytkownika")
            
   return render_template('singup.html',  form=loginform,message="")
   
#kontroller wyświetlający formularz rejestracji
@app.route("/register", methods=['GET','POST'])
def reg():
   
   registerform=register()
   message = '' 
   if request.method == 'POST': 
        if recaptcha.verify(): 
            
              if registerform.is_submitted():
                  result=request.form
      
                  add(result['username'],result['password1'],int(result['age']),result['email'])
     
        else:
            message = 'Wypełnij poprawnie Captasha'
   return render_template('register.html',registerform=registerform, message=message)
LogUser= Userr()

@app.route("/main",methods=['GET','POST'])

def mainWeb():
    if LogUser.username==None:
      
       return redirect("/loginn")

    if 'login' in session:              
      lista=getTop3Users()
      news=getNews()
      zalogowany = 'login' in session
      login = LogUser.username
      session['login'] = login
      data  = request.cookies.get(login)
      resp = make_response(render_template('main.html',data=data,  list=lista, zalogowany=zalogowany,LoggedUser=LogUser.username, login=login,news=news))
      
      print(data)
      return resp
    return redirect("/")
@app.route("/editGlo/<int:id>", methods=['GET','POST'])
def edit(id):
     x=sessions.query(Glo).filter(Glo.id==id).first()
     register=registerGlo()
     if request.method == 'POST': 
         if register.is_submitted():
           result=request.form
           sessions.query(Glo).filter(Glo.id==id).delete()
           sessions.add(result)
    
     return render_template("EditGlo.html", form = register, glo=x)
#kontroler wyświetlający dane użytkownika
@app.route("/userdata/<logi>", methods=['GET','POST'])
def editData(logi):
     user = Userr()
     user= get(logi)
     registerform=Edit()
     if request.method == 'POST': 
         if registerform.is_submitted():
                  result=request.form
                  if session['login']==logi:
                     updateData(user,result)
                  
                  return redirect("/")
     
     return render_template("userdata.html", LoggedUser= user,registerform = registerform)
#wyświetlenie bestiariusza
@app.route("/bestiariusz",methods=['GET','POST'])
def best():
      if LogUser.username==None:
      
       return redirect("/loginn")
      get = getBeasts()
      
      print('login' in session)
      if not 'login' in session:
         return f'nie jesteś zalogowany'
         
      else:
         return render_template("beast.html", result=get,user=LogUser)
  
#kontroller wyświetlający informacje o pojedyńczym potworze
@app.route("/beastinfo/<int:id>", methods=['GET','POST'])
def getBeastInfo(id):
   x=sessions.query(Beast).filter(Beast.id==id).first()
   return render_template("beastinfo.html",result=x, user = LogUser)
#kontroler wyświetlający informacje o pojedyńczej postaci
@app.route("/gloinfo/<int:id>", methods=['GET','POST'])
def getGloInfo(id):
   if LogUser.username==None or not 'login' in session:
      
       return redirect("/loginn")
  
   x=sessions.query(Glo).filter(Glo.id==id).first()
   return render_template("GloInfo.html",result=x, user = LogUser)
#kontroller wyświetlający formularz dodawnia potwora do bestiariusza
@app.route("/addBeast", methods=['GET','POST'])
def dodaj():
   loginform= registerBeast()
   if request.method == 'POST':
         if loginform.is_submitted():
            result=request.form
            dodajBeast(result)
   return render_template("AddBeast.html",form=loginform)

#kontroller przyjumjący id potwora i usuwający go z bazy danych
@app.route("/delB/<id>",methods=['GET','POST'])
def deletee(id):
   sessions.query(Beast).filter(Beast.id==id).delete()
   sessions.commit()
   return redirect("/bestiariusz")
#kontroller przyjumujący id postaci i usuwający ją z bazy danych
@app.route("/delG/<id>",methods=['GET','POST'])
def deleteeG(id):
   sessions.query(Glo).filter(Glo.id==id).delete()
   sessions.commit()
   return redirect("/glosariusz")
#kontroller dodający postać do glosarisza
@app.route("/addGlo",methods=['GET','POST'])
def addGloo():
   create()
   register=registerGlo()
   if request.method == 'POST':
      if register.is_submitted():
         result=request.form
         addGlo(result)
   return render_template("AddGlo.html", form=register)
#funkcja pobierania wszystkich użytkownikow i przefiltrowania 3 z najwieksza liczba wejść
def getTop3Users():
  oldList=Top3()
  newList={}
  for i in range(0,3):
   y=max(oldList, key=oldList.get)
   newList[y]=oldList[y]
   oldList.pop(y)
  return newList

#kontroler glosariusza
@app.route("/glosariusz",methods=['GET','POST'])
def glos():
      if LogUser.username==None:
       return redirect("/loginn")
      GloArray = getGlo()
      if not 'login' in session:
         return f'nie jesteś zalogowany'
        
      else:
       return render_template("Glo.html", result=GloArray,user=LogUser)
#kontroler dodania nowego newsa
@app.route("/addNews",methods=['GET','POST'])
def addNew():
      newsform = News()
      if newsform.is_submitted():
         result2=request.form
         addNews(result2)
      return render_template("news.html", form=newsform)
@app.route("/delNews/<id>",methods=['GET','POST'])
def delNew(id):
     delNews(id)
     return redirect("/main")
      



@app.route("/wallpapers")
def wallpapers():
    print('login' in session)
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    length=len(files)
    if not 'login' in session:
        return f'nie jesteś zalogowany'
    else:return render_template("wallpapers.html", lista=files,user=LogUser, x=length)
@app.route("/download/<src>")
def download(src):
    path = "static/wallpapers/"+src
    return send_file(path, as_attachment=True)
@app.route("/unlog")
def unlog():
   session.pop('login',None)
   global LogUser
   LogUser=None
   return redirect("/")

