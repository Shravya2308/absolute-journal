from absjl import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), nullable=False, unique=True)
    last_name = db.Column(db.String(15), nullable=False, unique=True)
    # email_id= db.Column(db.String(15), nullable=False, unique=True)
    # password = db.Column(db.String(300), nullable=False)
    # profile_pic = db.Column(db.String(300), nullable=False)