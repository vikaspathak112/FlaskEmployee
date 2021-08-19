from employee import app,models, db
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from employee.forms import AddEmployeeForm, UpdateEmployeeForm, DeleteEmployeeForm, EmployeeSearchForm
from employee.models import Employee

ROWS_PER_PAGE = 3
@app.route('/')
@app.route('/home')
def home_page():
	
	first_name = request.args.get('first_name',"",type=str)
	last_name = request.args.get('last_name',"",type=str)
	eid = request.args.get('eid',-1,type=int)
	page = request.args.get('page',1,type=int)

	search_form = EmployeeSearchForm()

	employees = Employee.query.order_by(Employee.first_name, Employee.last_name, Employee.eid).paginate(page=page, per_page=ROWS_PER_PAGE) 

	temp_emps = db.session.query(Employee)
	if first_name != "":
		temp_emps = temp_emps.filter_by(first_name=first_name)
	if last_name != "":
		temp_emps = temp_emps.filter_by(last_name=last_name)
	if eid != -1:
		temp_emps = temp_emps.filter_by(eid=eid)

	if first_name != "" or last_name != "" or eid != -1:
		print("FILTER PRESENT")
		employees = temp_emps.order_by(Employee.first_name, Employee.last_name, Employee.eid).paginate(page=page, per_page=ROWS_PER_PAGE) 
	
	
	return render_template('home.html',  search_form=search_form, employees=employees)

@app.route('/add', methods = ['GET', 'POST'])
def add_page():
	form = AddEmployeeForm()
	message = ''
	if form.validate_on_submit():
		if Employee.query.filter_by(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data).first() is not None:
			message = f'Employee with name {form.first_name.data} {form.last_name.data} and email {form.email.data} already exists'
		else:
			employee = Employee(first_name=form.first_name.data,
							last_name = form.last_name.data, 
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
		num_rows_updated = Employee.query.filter_by(eid=kwargs['eid']).update({'first_name':form.first_name.data,
																	'last_name':form.last_name.data,
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
