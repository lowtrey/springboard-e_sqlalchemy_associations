from models import Department, Employee, db
from app import app

# Create All Tables
db.drop_all()
db.create_all()

marketing = Department(dept_code="mktg", dept_name="Marketing", phone="555-1234")
accounting = Department(dept_code="acct", dept_name="Accounting", phone="555-1233")
james = Employee(name="James Jameson", state="NY", dept_code="mktg")
tina = Employee(name="Tina Tinashe", state="CA", dept_code="acct")
summer = Employee(name="Summer Ranaldson", state="AL", dept_code="mktg")

# Seperate Commits For Each Object Type
db.session.add(marketing)
db.session.add(accounting)
db.session.commit()

db.session.add(james)
db.session.add(tina)
db.session.add(summer)
db.session.commit()