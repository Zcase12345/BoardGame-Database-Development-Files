#here we will define the information for login/signup/sign out
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       email = request.form.get('email')
       password = request.form.get('password')
       
       user = User.query.filter_by(email=email).first()
       
       if user:
           if check_password_hash(user.password, password):
               flash('Successfully logged in!', category='success')
               login_user(user, remember=True)
               return redirect(url_for('views.home'))
           else:
               flash('Password is not correct. Try again.', category='error')
               return render_template("login.html", user=current_user)
       else:
           flash('This email does not exist.', category='error')
           return render_template("login.html", user=current_user)
           
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user() 
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('This email already exists.', category='error')
            return render_template("sign_up.html", user=current_user)
        elif username_exists:
            flash('This username already exists. Please choose another.', category='error')
            return render_template("sign_up.html", user=current_user)
        elif len(email) < 4:
            flash('Email must be at least 4 characters long.', category='error')
            return render_template("sign_up.html", user=current_user)
        elif len(username) < 2:
            flash('First name must be at least 2 characters long.', category='error')
            return render_template("sign_up.html", user=current_user)
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
            return render_template("sign_up.html", user=current_user)
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters long.', category='error')
            return render_template("sign_up.html", user=current_user)
        else:
            try:
                new_user = User(email=email, username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                flash('Account has been successfully created!', category='success')
                return redirect(url_for('views.home'))
            except Exception as e:
                db.session.rollback()
                flash(f'An error occurred: {str(e)}', category='error')
                return render_template("sign_up.html", user=current_user)
    
    return render_template("sign_up.html", user=current_user)
