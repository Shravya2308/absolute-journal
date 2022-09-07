from flask import Flask, render_template, redirect, request, session
from absjl import app

@app.get('/login')
def login():    
    return render_template('login.html')


@app.post('/login')
def login_post():
    data = request.get_json()
    username = data['username']
    password = data['password']
    print(username + "    " + password)
    data.update({"status": "ok"})
    with open('sexy.txt', 'w') as f:
        f.write(str(data))
    return data

@app.get('/logindata')
def login_data():
    file1 = open("sexy.txt","r+") 
    k = file1.read()
    return k

#     user = User.query.filter_by(username=username).first()

#     if user is None:
#         res_obj = {}
#         res_obj.update({"status": 1})
#         # user does not exist
#         res_obj.update({"error": "User doesnt exist so Go and <a href='/register'>Register</a>"})
#         return json.dumps(res_obj)
#     else:
#         if bcrypt.checkpw(password.encode('utf-8'),user.password):
#             session['uid'] = user.id
#             res_obj = {}
#             res_obj.update({"status": 0})
#             res_obj.update({"info": 'successful login'})
#             res_obj.update({"uid": session['uid']})
#             return json.dumps(res_obj)
#         else:
#             res_obj = {}
#             res_obj.update({"status": 1})
#             res_obj.update({"error": 'incorrect password'})
#             return json.dumps(res_obj)