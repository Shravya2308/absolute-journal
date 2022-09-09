from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dkljsakljdlksajlk'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///absjl.db'
db = SQLAlchemy(app)

from absjl.routes import login
from absjl.routes import home
from absjl.routes import teachers
from absjl.routes import teachnotes
from absjl.routes import year1
from absjl.routes import year2
from absjl.routes import year3
from absjl.routes import year4
from absjl.routes import about
from absjl.routes import blog
from absjl.routes import signup
from absjl.routes import functionalities
