from employee import db

class Employee(db.Model):
	eid = db.Column(db.Integer(), primary_key = True)
	first_name = db.Column(db.String(length=30), nullable=False)
	last_name = db.Column(db.String(length=30), nullable=False)
	email = db.Column(db.String(length=50), nullable=False, unique = True)
	position = db.Column(db.String(length=20), nullable=False)
	dept = db.Column(db.String(length=50), nullable=False) #consider making dept a different table later on keeping normalisation in mind
	salary = db.Column(db.Integer())

	def __repr__(self):
		return f'{self.eid}-{self.name}'