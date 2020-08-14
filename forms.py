from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField

class AddSnackForm(FlaskForm):
  """Form for adding snacks."""

  name = StringField("Snack Name")

  price = FloatField("Price in USD")

  quantity = IntegerField("How Many?")

  is_healthy = BooleanField("This is a healthy snack")

  # category = RadioField("Category", choices=[("ic", "Ice Cream", ), ("chips", "Potato Chips"), ("candy", "Candy/Sweets")])

  category = SelectField("Category", choices=[("ic", "Ice Cream", ), ("chips", "Potato Chips"), ("candy", "Candy/Sweets")])


class NewEmployeeForm(FlaskForm):
  """Form for adding employee"""

  name = StringField("Employee Name")

  state = StringField("State")

  department_code = StringField("Department Code")
