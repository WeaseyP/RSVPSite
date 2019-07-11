from flask import render_template, flash, redirect, url_for
from rsvp import application, db, bcrypt
from rsvp.forms import RegistrationForm, LoginForm, RSVPForm, EmailForm
from rsvp.models import User, RSVP
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user, logout_user, login_required



@application.route("/")
@application.route("/home")
def home():
    return render_template('index.html',title="Parsons Wedding 2019")


@application.route("/rsvp.html", methods=['GET','POST'])
def rsvp():
    if current_user.is_authenticated:
        return redirect(url_for('rsvpforms'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('rsvpforms'))
        
        else:
            flash('Login Unsuccessful. Please Check username and password', 'danger')
    return render_template('rsvp.html',title="RSVP", form=form)


@application.route("/register.html",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password = hashed_password, party_of = form.party_of.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('rsvp'))
    return render_template('register.html', title='Register', form=form)


@application.route("/rsvpforms.html",methods=['GET','POST'])
@login_required
def rsvpforms():
    form = RSVPForm()

    party_list = []
    party = int(current_user.party_of)
    i = 0
    while i<=party:
        party_list.append(i)
        i += 1
    form.party_attending.choices = [(a, a) for a in party_list] 

    if form.validate_on_submit():
        rsvp = RSVP(party_attending = form.party_attending.data, attending = form.attending.data, food = form.food.data, music = form.music.data, note = form.note.data, user_id = current_user.username)
        db.session.add(rsvp)
        db.session.commit()
        if int(form.party_attending.data) >= 1:
            return redirect(url_for('coming'))
        else:
            return redirect(url_for('sorry'))
    return render_template('rsvpforms.html', title='RSVPFORM', form=form)

@application.route("/coming.html",methods=['GET','POST'])
def coming():
    form = EmailForm()
    email = form.email.data
    if email:
        email = form.email.data
        print(email)
    return render_template('coming.html', title='Congrats!', form=form)

@application.route("/sorry.html",methods=['GET','POST'])
def sorry():
    return render_template('sorry.html', title='Sorry!')

@application.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



@application.errorhandler(404)  
def not_found(e):  
  return render_template("404.html") 