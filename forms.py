from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket
class CheckoutForm(FlaskForm):
    firstname = StringField("First Name", validators=[InputRequired()])
    lastname = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Email Address", validators=[InputRequired(), email()])
    phone = StringField("Phone Number", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    submit = SubmitField("Submit order")

