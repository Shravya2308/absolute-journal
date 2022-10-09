from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import db, Subject
import json

@app.post('/thread')
def thread():
    if not 'email_id' in session:
        res_obj = {}
        res_obj.update({"status": 1})
        res_obj.update({"error": 'not logged in'})
        return json.dumps(res_obj)
    else:
        email_id = session['email_id']
        posts = db.session.query(Subject).all()
        posts_list = []
        for i in range(0,len(posts)):
            tmp_dict = {}
            # tmp_dict.update({"id":i[1].id})
            tmp_dict.update({"name":posts[i].name})
            tmp_dict.update({"year_no":posts[i].year_no})
            tmp_dict.update({"sem_no":posts[i].sem_no})
            posts_list.append(tmp_dict)
        return json.dumps(posts_list)