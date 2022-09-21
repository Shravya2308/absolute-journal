from absjl import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email_id = db.Column(db.String(30),  nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False,unique=False)
    firstname = db.Column(db.String(15), nullable=False, unique=False)
    lastname = db.Column(db.String(15), nullable=False, unique=False)
    # email_id= db.Column(db.String(15), nullable=False, unique=True)
    # password = db.Column(db.String(300), nullable=False)
    # profile_pic = db.Column(db.String(300), nullable=False)

class Upload(db.Model):
    upload_id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    