from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from rsvp.models import User
from flask_login import current_user
import flask_login
from flask import session
from rsvp import db

from flask import render_template, flash, redirect, url_for
from rsvp import application, db, bcrypt
from rsvp.models import User, RSVP
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user

from rsvp import db
from datetime import datetime
from flask_login import UserMixin
from flask_login import current_user
from rsvp.models import User, RSVP




class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=4, max=30)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), EqualTo('password')])
    party_of = StringField('Party Of', validators=[DataRequired()])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                'That username is taken. Please choose a different one')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=4, max=30)])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')


class RSVPForm(FlaskForm):
    filenames = [0,1]


    party_attending = SelectField(u"Filename",  coerce =int)
    print(filenames)



    attending = TextAreaField('Enter Names of Attendees')

    food = TextAreaField('Special Food Requirements')

    music = TextAreaField('Music Requests')

    note = TextAreaField('Note for the Bride and Groom')

    submit = SubmitField('RSVP')


class EmailForm(FlaskForm):

    email = StringField('Please enter your email')
    submit = SubmitField('Submit')