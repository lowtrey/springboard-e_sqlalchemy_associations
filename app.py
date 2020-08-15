from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Department, Employee, Project, EmployeeProject, get_directory, get_directory_join
from forms import AddSnackForm, EmployeeForm

app = Flask(__name__)

# Configure and Initialize Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Configure Debug Toolbar
app.config['SECRET_KEY'] = "chickens"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def home_page():
  return render_template("home.html")

@app.route("/phones")
def list_phones():
  employees = Employee.query.all()
  return render_template("phones.html", employees=employees)


@app.route("/snacks/new", methods=["GET", "POST"])
def add_snack():
  form = AddSnackForm()
  # Is this a post request? AND Is the token valid?
  if form.validate_on_submit():
    name = form.name.data
    price = form.price.data
    flash(f"Created new snack: name is {name}, price is {price}")
    return redirect("/")
  else:
    return render_template("add_snack_form.html", form=form)


@app.route("/employees/new", methods=["GET", "POST"])
def add_employee():
  form = EmployeeForm()

  # Dynamically Add Department Choices
  # First item in tuple is value, second is what user sees
  departments = db.session.query(Department.dept_code, Department.dept_name)
  form.dept_code.choices = departments

  if form.validate_on_submit():
    name=form.name.data
    state=form.state.data
    dept_code=form.dept_code.data

    employee = Employee(name=name, state=state, dept_code=dept_code)
    
    db.session.add(employee)
    db.session.commit()
    return redirect("/phones")
  else:
    return render_template("add_employee_form.html", form=form)

@app.route("/employees/<int:id>/edit", methods=["GET", "POST"])
def edit_employee(id):
  # Pass in existing Employee to form
  # Object attributes must match form fields
  employee = Employee.query.get_or_404(id)
  form = EmployeeForm(obj=employee)

  # Dynamically Add Department Choices
  # First item in tuple is value, second is what user sees
  departments = db.session.query(Department.dept_code, Department.dept_name)
  form.dept_code.choices = departments

  if form.validate_on_submit():
    employee.name = form.name.data
    employee.state = form.state.data
    employee.dept_code = form.dept_code.data
    db.session.commit()
    return redirect("/phones")
  else:
    return render_template("edit_employee_form.html", form=form)
