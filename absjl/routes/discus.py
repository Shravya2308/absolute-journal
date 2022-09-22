from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/discus')
def discus():    
    return render_template('discus.html')