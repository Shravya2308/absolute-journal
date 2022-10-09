from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import Posts, db, Subject , Student
import json
import bcrypt
import bleach
import datetime

@app.post('/posts')
def recvpost():
    print(session)
    if not 'email_id' in session:
        res_obj = {}
        res_obj.update({"status": 1})
        res_obj.update({"error": 'not logged in'})
        return json.dumps(res_obj)
    else:
        data = request.get_json()
        new_content = data['content']
        new_content = bleach.linkify(bleach.clean(new_content))
        current_time = str(datetime.datetime.now())
        user = Student.query.get('Student.id')
        print(user)
        # temp_file_name = 'temp_posts/'+ str(session['uid'])
        # cmd = f'echo {new_content} > {temp_file_name}.txt'
        # r = os.popen(cmd)
        # comd = f'/usr/bin/curl -X POST -F file=@{temp_file_name}.txt ' + '"http://127.0.0.1:5001/api/v0/add"'
        # result = os.popen(comd)
        # a = json.loads(result.read())
        # new_content_hash = a['Hash']
        post = Posts(content=new_content,created=current_time, Student_id= user )
        db.session.add(post)
        db.session.commit()
        res_obj = {}
        res_obj.update({"status": 0})
        res_obj.update({"info": 'new post created successfully'})
        return json.dumps(res_obj)

         