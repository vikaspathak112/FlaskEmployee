from employee import app,models, db
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from employee.forms import AddEmployeeForm, UpdateEmployeeForm, DeleteEmployeeForm
from employee.models import Employee

ROWS_PER_PAGE = 3
@app.route('/')
@app.route('/home')
def home_page():
	
	page = request.args.get('page',1,type=int)
	print("PAGE REQUESTED: " + str(page))
	#employees = Employee.query.all()
	employees = Employee.query.paginate(page=page, per_page=ROWS_PER_PAGE) 
	return render_template('home.html', employees=employees)

@app.route('/add', methods = ['GET', 'POST'])
def add_page():
	form = AddEmployeeForm()
	message = ''
	if form.validate_on_submit():
		if Employee.query.filter_by(name=form.name.data, email=form.email.data).first() is not None:
			message = f'Employee with name {form.name.data} and email {form.email.data} already exists'
		else:
			employee = Employee(name=form.name.data, 
							email=form.email.data,
							position=form.position.data,
							dept=form.dept.data,
							salary=form.salary.data)
			db.session.add(employee)
			db.session.commit()
			message = 'Employee Added Successfully'
	else:
		print(form.errors)

	print(message)	
	#print(form.data)
	#print(type(form.data))	
	return render_template('add.html', form=form, message=message)

@app.route('/update/<eid>', methods = ['GET', 'POST'])
def update_page(**kwargs):
	form = UpdateEmployeeForm()
	employee_to_be_updated = Employee.query.filter_by(eid=kwargs['eid']).first()
	message = ''
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		num_rows_updated = Employee.query.filter_by(eid=kwargs['eid']).update({'name':form.name.data,
																	'email':form.email.data,
																	'position':form.position.data,
																	'dept':form.dept.data,
																	'salary':form.salary.data})
		db.session.commit()
		message = 'Employee Updated Successfully'
	return render_template('update.html', form=form, employee=employee_to_be_updated, message=message)

@app.route('/delete/<eid>', methods = ['GET', 'POST'])
def delete_page(**kwargs):
	form = DeleteEmployeeForm() 
	employee_to_be_deleted = Employee.query.filter_by(eid=kwargs['eid']).first()
	message = ''

	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		if employee_to_be_deleted is not None:
			db.session.delete(employee_to_be_deleted)
			db.session.commit()
			message='Employee Deleted Successfully'
		else:
			message='Employee Does Not Exist'

	return render_template('delete.html', form=form, employee=employee_to_be_deleted, message=message)
