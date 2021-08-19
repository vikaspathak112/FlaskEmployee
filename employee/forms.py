from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, IntegerField

class EmployeeForm(FlaskForm):
	first_name = StringField(label='First Name')
	last_name = StringField(label='Last Name')
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

class EmployeeSearchForm(FlaskForm):
	first_name = StringField(label='First Name')
	last_name = StringField(label='Last Name')
	eid = StringField(label='Employee ID')
	search = SubmitField(label='Search Employee')
