from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import Users

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('submit')


class UserRegistration(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    firstname = StringField('firstname',validators=[DataRequired()])
    lastname = StringField('lastname',validators=[DataRequired()])
    email = StringField('email',validators=[DataRequired(), Email()])
    password = PasswordField('password',validators=[DataRequired()])
    password2 = PasswordField('repeat password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('submit')
    
    def validate_username(self, username):
        returned_user = Users.query.filter_by(username=username.data).first()
        if returned_user is not None:
            raise ValidationError('please select a different username')

    def validate_email(self, email):
        returned_email = Users.query.filter_by(email=email.data).first()
        if returned_email is not None:
            raise ValidationError('please select a different email')
