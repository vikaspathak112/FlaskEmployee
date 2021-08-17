from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField

class EmployeeForm(FlaskForm):
	name = StringField(label='Name')
	email = StringField(label='Email')
	position = StringField(label='Position')
	dept = StringField(label='Department')
	salary = IntegerField(label='Salary') 

class AddEmployeeForm(EmployeeForm):
	add = SubmitField(label='Add')

class UpdateEmployeeForm(EmployeeForm):
	update = SubmitField(label='Update')

class DeleteEmployeeForm(EmployeeForm):
	delete = SubmitField(label='Delete')