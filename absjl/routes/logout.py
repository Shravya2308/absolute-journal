from flask import Flask,render_template,redirect,request,session
from absjl import app
from absjl import db,Student

@app.get('/logout')
def logout():
    if 'uid' in session:
       session.pop('email_id', None)
    return redirect('/')

@app.post('/logout')
def poslogout():
    if 'uid' in session:
       session.pop('email_id', None)
    return redirect('/')