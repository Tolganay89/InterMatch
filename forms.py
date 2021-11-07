from flask_wtf import Form
from wtforms import StringField


class StudentForm(Form):
    id_student_college = StringField(
        'id_student_college'
    )
    name = StringField(
        'name'
    )
    availability = StringField(
        'availability'
    )
    address = StringField(
        'address'
    )
    phone = StringField(
        'phone'
    )
    
