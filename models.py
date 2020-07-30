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


class Employee(db.Model):
  """Employee"""

  __tablename__ = "employees"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  name = db.Column(db.Text, nullable=False, unique=True)

  state = db.Column(db.Text, nullable=False, default="LA")

  # dept_code = db.Column(db.Text)