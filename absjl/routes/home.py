from flask import Flask, render_template, redirect, request, session
from absjl import app



@app.get('/')
@app.get('/home')
def home():    
    return render_template('home.html')