from absjl import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email_id = db.Column(db.String(30),  nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False,unique=False)
    # first_name = db.Column(db.String(15), nullable=True, unique=False)
    # last_name = db.Column(db.String(15), nullable=True, unique=False)
    # email_id= db.Column(db.String(15), nullable=False, unique=True)
    # password = db.Column(db.String(300), nullable=False)
    # profile_pic = db.Column(db.String(300), nullable=False)