from flask import Flask, render_template, redirect, request, session
from absjl.modals.dbschema import db, Student ,Subject ,Posts
from absjl import app
import json



@app.post('/getposts')
def getposts():
    posts = db.session.query(Posts).all()
    posts_list = []
    for i in range(0,len(posts)):
        tmp_dict = {}
        # tmp_dict.update({"id":i[1].id})
        tmp_dict.update({"name":posts[i].subject})
        tmp_dict.update({"year_no":posts[i].content})
        tmp_dict.update({"sem_no":posts[i].created})
        tmp_dict.update({"sem_no":posts[i].Student_id})
        tmp_dict.update({"sem_no":posts[i].Thread_id})
        posts_list.append(tmp_dict)    
    return json.dumps(posts_list)