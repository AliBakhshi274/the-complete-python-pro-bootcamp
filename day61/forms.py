from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, length
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), length(max=5)])
    password = PasswordField('Password', validators=[DataRequired(), length(min=5)])
    email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')