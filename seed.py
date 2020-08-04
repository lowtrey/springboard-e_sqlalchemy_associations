from models import Department, Employee, Project, EmployeeProject, db
from app import app

# Create All Tables
db.drop_all()
db.create_all()

# d1 = Department(dept_code="mktg", dept_name="Marketing", phone="555-1234")
# d2 = Department(dept_code="acct", dept_name="Accounting", phone="555-1233")
# d3 = Department(dept_code="r&d", dept_name="Research and Development", phone="222-1233")
# d4 = Department(dept_code="sales", dept_name="Sales", phone="222-5555")
# d5 = Department(dept_code="it", dept_name="Internet & Technology")

# james = Employee(name="James Jameson", state="NY", dept_code="mktg")
# tina = Employee(name="Tina Tinashe", state="CA", dept_code="acct")
# summer = Employee(name="Summer Ranaldson", state="AL", dept_code="mktg")
# caesar = Employee(name="Caesar Atavo", state="TX", dept_code="it")
# sonny = Employee(name="Sonny Boy", state="AZ", dept_code="r&d")
# ashley = Employee(name="Ashley Berns", state="HI", dept_code="sales")

# # Seperate Commits For Each Object Type
# db.session.add_all([d1, d2, d3, d4, d5])
# db.session.commit()

# db.session.add_all([james, tina, summer, caesar, sonny, ashley])
# db.session.commit()


EmployeeProject.query.delete()
Employee.query.delete()
Department.query.delete()
Project.query.delete()

# Add sample employees and departments
df = Department(dept_code='fin', dept_name='Finance', phone='555-1000')
dl = Department(dept_code='legal', dept_name='Legal', phone='555-2222')
dm = Department(dept_code='mktg', dept_name='Marketing', phone='555-9999')

leonard = Employee(name='Leonard', dept=dl)
liz = Employee(name='Liz', dept=dl)
maggie = Employee(name='Maggie', state='DC', dept=dm)
nadine = Employee(name='Nadine')

db.session.add_all([df, dl, dm, leonard, liz, maggie, nadine])
db.session.commit()

pc = Project(project_code='car', project_name='Design Car',
             assignments=[EmployeeProject(employee_id=liz.id, role='Chair'),
                          EmployeeProject(employee_id=maggie.id)])

ps = Project(project_code='server', project_name='Deploy Server',
             assignments=[EmployeeProject(employee_id=liz.id),
                          EmployeeProject(employee_id=leonard.id, role='Auditor')])

db.session.add_all([ps, pc])
db.session.commit()