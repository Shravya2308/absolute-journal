from flask import Flask, render_template, redirect, request, session
from absjl import app
from absjl.modals.dbschema import db, Upload
from werkzeug.utils import secure_filename
import os
from absjl import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get('/test')
def test_get():
    return render_template("test.html")

@app.post('/test')
def test():
    if request.method == 'POST':
        file = request.files['file']
        #file.save(secure_filename(file.filename))
        

        if allowed_file(file.filename) == True:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)
            # return 'file uploaded successfully'
            upload = Upload(filename=file.filename)
            db.session.add(upload)
            db.session.commit()
            return f"Hello, {file.filename}"
        else:
            return f"MARJA KUTTE, {file.filename}"
        
    
       
        
      
        
    
    return render_template('test.html')
