from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

# Models 
class Department(db.Model):
  """Department. A department has many employees"""

  __tablename__ = "departments"

  dept_code = db.Column(db.Text, primary_key=True)
  
  dept_name = db.Column(db.Text, nullable=False, unique=True)

  phone = db.Column(db.Text)

  def __repr__(self):
    return f"<Department {self.dept_code} {self.dept_name} {self.phone}>"


class Employee(db.Model):
  """Employee"""

  __tablename__ = "employees"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  name = db.Column(db.Text, nullable=False, unique=True)

  state = db.Column(db.Text, nullable=False, default="LA")

  # Foreign Key References table name, not Model name
  dept_code = db.Column(db.Text, db.ForeignKey("departments.dept_code"))

  # Add Department - Employee Relationship reference
  # backref = name of relationship you want
  # Can run: emp.dept.phone
  dept = db.relationship("Department", backref="employees")

  def __repr__(self):
    return f"<Employee {self.state} {self.name} {self.dept_code}>"


def get_directory():
  all_employees = Employee.query.all()
  
  for emp in all_employees:
    if emp.dept is not None:
      print(emp.name, emp.dept.dept_name, emp.dept.phone)
    else:
      print(emp.name)