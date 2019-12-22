from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from tasker.models import User


class LoginForm(FlaskForm):
    """User login form"""
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    """User registration form."""
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        """Unique username validation checks if given username is still available"""
        user = User.get_user_by_username(username=username.data)
        if user is not None:
            raise ValidationError('Please choose different username.')

    def validate_email(self, email):
        """Unique Email validation  checks if given email is still available"""
        user = User.get_user_by_email(email=email.data)
        if user is not None:
            raise ValidationError('Please choose different email.')
