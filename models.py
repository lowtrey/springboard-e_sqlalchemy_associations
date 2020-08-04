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

  assignments = db.relationship("EmployeeProject", backref="employee")

  def __repr__(self):
    return f"<Employee {self.state} {self.name} {self.dept_code}>"



class Project(db.Model):
  """Project. Employees can be assigned to this"""

  __tablename__ = "projects"

  project_code = db.Column(db.Text, primary_key=True)

  project_name = db.Column(db.Text, nullable=False, unique=True)

  assignments = db.relationship("EmployeeProject", backref="project")


class EmployeeProject(db.Model):
  """Mapping of an employee to a project"""

  __tablename__ = "employees_projects"

  # Set up combined primary key by setting multiple columns to True
  employee_id = db.Column(db.Integer, db.ForeignKey("employees.id"), primary_key=True)

  project_code = db.Column(db.Text, db.ForeignKey("projects.project_code"), primary_key=True)

  role = db.Column(db.Text)



def get_directory():
  all_employees = Employee.query.all()
  
  for emp in all_employees:
    if emp.dept is not None:
      print(emp.name, emp.dept.dept_name, emp.dept.phone)
    else:
      print(emp.name)

# Returns Tuples
def get_directory_join():
  directory = db.session.query(Employee.name, Department.dept_name, Department.phone).join(Department).all()

  for name, dept, phone in directory:
    print(name, dept, phone)

# Returns Class Objects 
def get_directory_join_class():
  directory = db.session.query(Employee, Department).join(Department).all()

  for emp, dept in directory:
    print(emp.name, dept.dept_name, dept.phone)