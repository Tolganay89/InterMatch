#----------------------------------------------------------------------------#
# Imports
# how to run it 
# FLASK_APP=app.py FLASK_DEBUG=1 flask run 
#----------------------------------------------------------------------------#
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
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

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  db.create_all()
    # db.app = app
    # # db.init_app(app)
    # db.create_all()

  return render_template('pages/home.html')


#  Students
#  ----------------------------------------------------------------
"""
show all the st
"""
@app.route('/students')
def students():

  print("hello")
  stus = db.session.query(Student).all()
  print(stus)
  data = []

  for s in stus:
        # student = Student.query.filter(Student.id == area.id).filter(Venue.id == area.id).all()
  
        data.append({ 'id': s.id, 'name': s.name })

  

  return render_template('pages/students.html', areas=data);

"""
create an endpoint for the search the of the students
"""
@app.route('/students/search', methods=['POST'])
def search_student():

  term = request.form.get('search_term', '')

  # seach for student should return student with that name
  result = db.session.query(Student).filter(Student.name.ilike(f'%{term}%')).all()

  response = {
    "count":len(result),
    "data": result
  }

  # create search_students page to do in the future.
  return render_template('pages/search_students.html', results=response, search_term=request.form.get('search_term', ''))

"""
show all the student endpoint 
"""
@app.route('/students/<int:student_id>')
def show_student(student_id):
  # shows the student page with the given student_id

  # 1. getting the data from the db
  student = Student.query.get(student_id)

  # 2. if not found
  if student is None:
        print('error')
        abort(404)

  data = {
    "id": student.id,
    "id_student_college": student.id_student_college,
    "name": student.name,
    "availability": student.availability,
    "address": student.address,
    "phone": student.phone, 
    "interviews": student.interviews
    
    }

  # create search_students page to do in the future.
  return render_template('pages/show_student.html', student=data)

#----------------------------------------------------------------------------#
# Launch.
#------------------------------------------------------------------ ----------#

# Default port:
if __name__ == '__main__':
    app.run()