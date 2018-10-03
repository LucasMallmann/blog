from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired('This field is required'),
        Length(min=2, max=20)]
    )

    email = StringField(
        'Email',
        validators=[DataRequired('This field is required'), Email()]
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is already takem. Please choose another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already takem. Please choose another one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired('This field is required'), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('rembember me')
    submit = SubmitField('Sign In')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('This field is required'),Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired('This field is required'), Email()])
    submit = SubmitField('Update')
    picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is already takem. Please choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is already takem. Please choose another one')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create')