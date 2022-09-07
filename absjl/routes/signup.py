from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student
from absjl import app
import json
import bcrypt
import bleach


@app.get('/signup')
def signup():    
    return render_template('login.html')


@app.post('/signup')
def signup_post():
    data = request.get_json()
    email_id= data['email_id']
    password = data['password']
    firstname = data['firstname']
    lastname = data['lastname']
    
    email  = Student.query.filter_by(email_id=email_id).first()

    if email is None:
        bytePwd = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(bytePwd,salt)
        tmp_student = Student(email_id=email_id,password=hashed,firstname=firstname,lastname=lastname)
        db.session.add(tmp_student)
        db.session.commit()
        res_obj = {}
        res_obj.update({"status":"OK"})
        res_obj.update({"message":"Successful !. Please go ahead and login"})
        return json.dumps(res_obj)
    else:
        res_obj = {}
        res_obj.update({"status":"ERROR"})
        res_obj.update({"error":"Email already registered with"})
        return json.dumps(res_obj)

        

       




    return data