from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/upvote')
def upvote():    
    return render_template('upvote.html')