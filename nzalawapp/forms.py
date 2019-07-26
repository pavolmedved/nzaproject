from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,Email
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("confirm Password", validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField()

class ReviewForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(),Email()])
    review = TextAreaField("Review Form", validators=[DataRequired()])
    submit = SubmitField()

class ContactForm(FlaskForm):
    full_name = StringField("Full Name", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    email_address = StringField("Email Address", validators=[DataRequired()])
    submit = SubmitField()
