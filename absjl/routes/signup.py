from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/signup')
def signup():    
    return render_template('login.html')


@app.post('/signup')
def signup_post():
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    print(username + "    " + email + "    " + password)
    return data