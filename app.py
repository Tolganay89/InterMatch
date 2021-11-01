#----------------------------------------------------------------------------#
# Imports
# how to run it 
# FLASK_APP=app.py FLASK_DEBUG=1 flask run 
#----------------------------------------------------------------------------#
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler



#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#
app = Flask(__name__)

db = SQLAlchemy(app)

app.config.from_object('config')
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Student(db.Model):
      # Tier column 
      # proiporty are the student 
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    id_student_college= db.Column(db.Integer)
    name = db.Column(db.String)
    availability = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    interviews = db.relationship('Interview', backref='student', lazy=True)


    def __repr__(self):
        return f'<student id: {self.id_student_college} name: {self.name}>'
class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name_company = db.Column(db.String)
    name_interviewer = db.Column(db.String)
    availability = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    interviews = db.relationship('Interview', backref='Company', lazy=True)


    def __repr__(self):
        return f'<Company id: {self.id} name company: {self.name_company}  name interviewer: {self.name_interviewer}>'

class Interview(db.Model):
    __tablename__ = 'interview'

    id = db.Column(db.Integer, primary_key=True)
    id_student= db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    id_company  = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    match_availability = db.Column(db.String(120),nullable=False)

    def __repr__(self):
        return f'<interview id: {self.id} student id: {self.id_student} company interviewer id: {self.id_company}  match_availability: {self.match_availability}>'

@app.route("/")
def hello_world():
    db.app = app
    # db.init_app(app)
    db.create_all()
    return "<p>Hello, World!</p>"
