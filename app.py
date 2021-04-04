import os
import datetime
from flask import (
    Flask, flash, render_template, request, url_for,
    redirect, session, Markup)
# for password hashing
from werkzeug.security import (
    generate_password_hash, check_password_hash)
from flask_sqlalchemy import SQLAlchemy
from models import User, Review
from sqlalchemy.sql import func
if os.path.exists('env.py'):
    import env


# configure app
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

# configure DB
# bug fix/workaround: https://github.com/pallets/flask-sqlalchemy/issues/929
app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initiate connection to DB
db = SQLAlchemy(app)


# route for Home (landing) page
@app.route('/')
def home():
    return render_template('index.html')


# route for Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        firstname = data.get('register-form-first-name')
        lastname = data.get('register-form-last-name')
        email = data.get('register-form-email')
        password1 = data.get('register-form-password1')
        password2 = data.get('register-form-password2')

        # Register form validation and categorised flash messaging conditional logic
        if firstname == '' or lastname == '' or email == '' or password1 == '' or password2 == '':
            message = Markup('Please fill out all fields!<br><i class="fas all-required-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(firstname) > 0 and len(firstname) < 2:
            message = Markup('Your first name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(lastname) > 0 and len(lastname) < 2:
            message = Markup('Your last name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 0 and len(email) < 6:
            message = Markup('Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) > 0 and len(password2) > 0 and password1 != password2:
            message = Markup('Your passwords don\'t match!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(firstname) >= 2 and len(lastname) >= 2 and len(email) >= 6 and password1 == password2:

            # Check to see if user/email entered already exists in DB
            if db.session.query(User).filter(User.email == email).count() == 0:
                # flash msg here to confirm user registration upon redirect
                message = Markup('Thanks for registering, {} <i class="fas fa-cut"></i></br>Welcome to the Clipadvisor community!</br>Is there a new barber you\'d like to tell us about?'.format(firstname))
                flash(message, 'success')

                new_user = User(
                                firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(
                                    password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                
                # Store newly-registered user in session cookie
                session['user'] = data.get('register-form-email')

                return redirect(url_for('review_submit'))
            message = Markup('There is already an account associated with that email! Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')   
    return render_template('register.html')


# route for Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('login-email')
        password = data.get('login-password')

        # Login form validation and categorised flash messaging conditional logic
        if email == '' or password == '':
            message = Markup('Please fill out all fields!<br><i class="fas all-required-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(email) > 0 and len(email) < 6:
            message = Markup('Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) >= 6:
        # Check to see if user/email entered already exists in DB
            if db.session.query(User).filter(User.email == email).count() != 0:

                # verify that login password matches hashed password stored in DB
                login_user = db.session.query(User).filter(User.email == email)
                if login_user.count() != 0:
                    if check_password_hash(
                                login_user[0].password, password):
                        message = Markup('Nice to see you, {} <i class="fas fa-cut"></i></br>Is there a new barber you\'d like to tell us about?'.format(
                            login_user[0].firstname))
                        flash(message, 'success')

                        # Store logged-in user in session cookie
                        session['user'] = data.get('login-email')

                        return redirect(url_for('review_submit'))
                    else:
                        # Deliberately ambiguous message to prevent malicious brute-force login attempts
                        message = Markup('You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
                        flash(message, 'warning')
            else:
                # Another deliberately ambiguous message to prevent malicious brute-force login attempts
                message = Markup('You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
                flash(message, 'warning')
    return render_template('login.html')


# route for login page
@app.route('/logout')
def logout():

    user = User.query.filter_by(email=session['user']).first()

    print(user.firstname)
    message = Markup('Thanks for being a part of Clipadvisor, {} <i class="fas fa-cut"></i></br>You have logged out successfully.<br>We hope to see you again soon!'.format(user.firstname))
    flash(message, 'success')

    # Remove/Destroy session cookie associated with user
    session.pop('user')

    return render_template('logout.html')


# route for Barbers page
@app.route('/barbers')
def barbers():
    return render_template('barbers.html')


# route for Submit A Review page
@app.route('/review-submit', methods=['GET', 'POST'])
def review_submit():

    # user_email = db.session.query(
    #     User).filter(User.email == session['user']).count()
    user_email = session['user']
    user = User.query.filter_by(email=session['user']).first()
    user_id = user.id
    users = User.query.all()

    if request.method == 'POST':
        data = request.form
        customername = data.get('review-submit-form-customer-name')
        barbershopname = data.get('review-submit-form-barbershop-name')
        date = data.get('review-submit-form-date-picker')
        time = data.get('review-submit-form-time-picker')
        cash = data.get('review-submit-form-payment-cash-checkbox')
        card = data.get('review-submit-form-payment-card-checkbox')
        vibe = data.get('review-submit-form-vibe')
        rating = data.get('review-submit-form-star-rating')
        comments = data.get('review-submit-form-comments')
        user_id = user_id
        phone = data.get('review-submit-form-booking-phone-checkbox')
        online = data.get('review-submit-form-booking-online-checkbox')
        walkin = data.get('review-submit-form-booking-walkin-checkbox')

        # flash msg here to confirm user registration upon redirect
        message = Markup('Thanks for rating your barber!<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
        flash(message, 'success')

        new_review = Review(
            customername=customername, barbershopname=barbershopname, date=date, time=time, cash=cash, card=card, vibe=vibe, rating=rating, comments=comments, user_id=user_id, phone=phone, online=online, walkin=walkin)
        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for('reviews'))

    return render_template(
        'review-submit.html', user=user)


# route for Reviews page
@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    reviews.reverse()
    return render_template('reviews.html', reviews=reviews)


# route for Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


# SANDBOX
@app.route('/sandbox')
def sandbox():
    return render_template('sandbox.html')


if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP'), port=5000)
