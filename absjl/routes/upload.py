from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/upload')
def upload():    
    return render_template('upload.html')