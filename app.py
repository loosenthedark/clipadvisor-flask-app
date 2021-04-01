import os
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


# Configure app
app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

# Configure DB
# Bug fix/workaround: https://github.com/pallets/flask-sqlalchemy/issues/929
app.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI')
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initiate connection to DB
db = SQLAlchemy(app)


# Route for Home (landing) page
@app.route('/')
def home():
    return render_template('index.html')


# Route for Registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        firstname = data.get('register-form-first-name')
        lastname = data.get('register-form-last-name')
        email = data.get('register-form-email')
        password1 = data.get('register-form-password1')
        password2 = data.get('register-form-password2')

        # Form validation and categorised flash messaging conditional logic
        if len(firstname) < 2:
            flash('Please enter a first name with a minimum of 2 characters!', 'warning')
        if len(lastname) < 2:
            flash('Please enter a last name with a minimum of 2 characters!', 'warning')
        if len(email) < 6:
            message = Markup('Your email address is too short!</br>Please try again.')
            flash(message, 'warning')
        if password1 != password2:
            message = Markup('Your passwords don\'t match!</br>Please try again.')
            flash(message, 'warning')
        if len(firstname) >= 2 and len(lastname) >= 2 and len(email) >= 6 and password1 == password2:

            # Check to see if user/email entered already exists in DB
            if db.session.query(User).filter(User.email == email).count() == 0:
                # flash msg here to confirm user registration upon redirect
                message = Markup('Thanks for registering, {}!</br>Welcome to the Clipadvisor community &#128513;</br>Is there a new barber you\'d like to tell us about?'.format(firstname))
                flash(message, 'success')

                new_user = User(
                                firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(
                                    password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                print(new_user.id)
                # Store new registered user in session cookie
                session['user'] = data.get('register-form-email')
                print(session['user'])

                return redirect(url_for('review_submit'))
            message = Markup('There is already an account associated with that email! Please try again.')
            flash(message, 'warning')   
    return render_template('register.html')


# Route for Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('login-email')
        password = data.get('login-password')

        # Form validation and categorised flash messaging conditional logic
        # Check to see if user/email entered already exists in DB
        if db.session.query(User).filter(User.email == email).count() != 0:

            # verify that login password matches hashed password stored in DB
            login_user = db.session.query(User).filter(User.email == email)
            if login_user.count() != 0:
                if check_password_hash(
                            login_user[0].password, password):
                    message = Markup('Nice to see you, {}!</br>Is there a new barber you\'d like to tell us about?'.format(
                        login_user[0].firstname))
                    flash(message, 'success')
                    # Store logged-in user in session cookie
                    session['user'] = request.form.get('email')

                    returning_user=login_user[0]
                    return redirect(url_for('review_submit'))
                else:
                    # Deliberately ambiguous message to prevent brute-force login attempts
                    message = Markup('You have entered an invalid email/password.</br>Please try again!')
                    flash(message, 'warning')
        else:
            # Another deliberately ambiguous message to prevent brute-force login attempts
            message = Markup('You have entered an invalid email/password.</br>Please try again!')
            flash(message, 'warning')
    return render_template('login.html')


# Route for login page
@app.route('/logout')
def logout():

    return render_template('login.html')


# Route for Barbers page
@app.route('/barbers')
def barbers():
    return render_template('barbers.html')


# Route for Review Submit page
@app.route('/review-submit', methods=['GET', 'POST'])
def review_submit():

    # user_email = db.session.query(
    #     User).filter(User.email == session['user']).count()
    user_email = session['user']
    print(user_email)
    user = User.query.filter_by(email=session['user']).first()
    user_id = user.id
    print(user_id)
    users = User.query.all()
    print(users)

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
        review_timestamp = func.now()
        user_id = user_id

        # flash msg here to confirm user registration upon redirect
        message = Markup('Thanks for rating your barber!')
        flash(message, 'success')

        new_review = Review(
            customername=customername, barbershopname=barbershopname, date=date, time=time, cash=cash, card=card, vibe=vibe, rating=rating, comments=comments, review_timestamp=review_timestamp, user_id=user_id)
        db.session.add(new_review)
        db.session.commit()

        return redirect(url_for('reviews'))

    return render_template(
        'review-submit.html', user=user)


# Route for Reviews page
@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    print(type(reviews))
    reviews.reverse()
    return render_template('reviews.html', reviews=reviews)


# Route for Contact page
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
