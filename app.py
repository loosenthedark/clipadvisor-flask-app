import os
import datetime
from flask import (
    Flask, flash, render_template, request, url_for,
    redirect, session, Markup)
# for password hashing
from werkzeug.security import (
    generate_password_hash, check_password_hash)
from flask_sqlalchemy import SQLAlchemy
from models import User, Review, Vibe
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


# Home route (landing page)
@app.route('/')
def home():
    return render_template('index.html')


# route to register user
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
            message = Markup('Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(firstname) > 0 and len(firstname) < 2:
            message = Markup('Your first name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(firstname) > 50:
            message = Markup('Your first name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(lastname) > 0 and len(lastname) < 2:
            message = Markup('Your last name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(lastname) > 50:
            message = Markup('Your last name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 0 and len(email) < 6:
            message = Markup('Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 100:
            message = Markup('Your email address is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) > 0 and len(password2) > 0 and len(password1) < 8 or len(password2) < 8:
            message = Markup('Your password is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) > 100 or len(password2) > 100:
            message = Markup('Your password is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) >= 8 and len(password2) >= 8 and len(password1) < 100 and len(password2) < 100 and password1 != password2:
            message = Markup('Your passwords don\'t match!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        
        if len(firstname) >= 2 and len(firstname) <= 50 and len(lastname) >= 2 and len(lastname) <= 50 and len(email) >= 6 and len(email) <= 100 and len(password1) >= 8 and len(password2) >= 8 and len(password1) <= 100 and len(password2)<= 100 and password1 == password2:
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


# route to log user in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data.get('login-email')
        password = data.get('login-password')

        # Login form validation and categorised flash messaging conditional logic
        if email == '' or password == '':
            message = Markup('Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(email) > 0 and len(email) < 6:
            message = Markup('Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 100:
            message = Markup('Your email address is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

        if len(email) >= 6 and len(email) <= 100 and len(password) >= 8 and len(password) <=100:
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
                        # Deliberately ambiguous message to guard against malicious brute-force login attempts
                        message = Markup('You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
                        flash(message, 'warning')
            else:
                # Another deliberately ambiguous message to guard against malicious brute-force login attempts
                message = Markup('You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
                flash(message, 'warning')
    
        else:
            # Another deliberately ambiguous message to guard against malicious brute-force login attempts
            message = Markup('You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

    return render_template('login.html')


# route to log user out
@app.route('/logout')
def logout():

    user = User.query.filter_by(email=session['user']).first()

    message = Markup('Thanks for being a part of Clipadvisor, {} <i class="fas fa-cut"></i></br>You have logged out successfully.<br>We hope to see you again soon!'.format(user.firstname))
    flash(message, 'success')

    # Remove/Destroy session cookie associated with user
    session.pop('user')

    return render_template('logout.html')


# route to view all barbers
@app.route('/barbers')
def barbers():
    return render_template('barbers.html')


# route to submit a review
@app.route('/review-submit', methods=['GET', 'POST'])
def review_submit():

    user = User.query.filter_by(email=session['user']).first()
    user_id = user.id

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

        # Submit A Review form validation and categorised flash messaging conditional logic
        if customername == '' or barbershopname == '' or date == '' or time == '' or phone == '' and online == '' and walkin == '' or cash == '' and card == '' or vibe == '' or comments == ''  or rating == '':
            message = Markup('Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(customername) > 0 and len(customername) < 4:
            message = Markup('Your name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(customername) > 50:
            message = Markup('Your name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(barbershopname) > 0 and len(barbershopname) < 3:
            message = Markup('Your barber\'s name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(barbershopname) > 50:
            message = Markup('Your barber\'s name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(comments) > 0 and len(comments) < 10:
            message = Markup('Your comment is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(comments) > 1000:
            message = Markup('Your comment is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        
        if len(customername) >= 4 and len(customername) <= 50 and len(barbershopname) >= 3 and len(barbershopname) <= 50 and date != '' and time != '' and len(comments) >= 10 and len(comments) <= 1000 and rating != '':

            # flash msg here to confirm review submission upon redirect
            message = Markup('Thanks for rating your barber!<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
            flash(message, 'success')

            new_review = Review(
                customername=customername, barbershopname=barbershopname, date=date, time=time, cash=cash, card=card, vibe=vibe, rating=rating, comments=comments, user_id=user_id, phone=phone, online=online, walkin=walkin)
            db.session.add(new_review)
            db.session.commit()

            return redirect(url_for('reviews'))

    return render_template(
        'review-submit.html', user=user)


# route to view all reviews
@app.route('/reviews')
def reviews():

    current_user = User.query.filter_by(email=session['user']).first()
    reviews = Review.query.all()
    return render_template('reviews.html', user=current_user, reviews=reviews)


# route to update a review
@app.route('/review_update/<review_id>', methods=['GET', 'POST'])
def review_update(review_id):

    user = User.query.filter_by(email=session['user']).first()
    user_id = user.id

    if request.method == 'POST':

        data = request.form
        updated_review = db.session.query(Review).filter(Review.id == review_id).first()
        updated_review.customername = data.get('review-update-form-customer-name')
        updated_review.barbershopname = data.get('review-update-form-barbershop-name')
        updated_review.date = data.get('review-update-form-date-picker')
        updated_review.time = data.get('review-update-form-time-picker')
        updated_review.cash = data.get('review-update-form-payment-cash-checkbox')
        updated_review.card = data.get('review-update-form-payment-card-checkbox')
        updated_review.vibe = data.get('review-update-form-vibe')
        updated_review.rating = data.get('review-update-form-star-rating')
        updated_review.comments = data.get('review-update-form-comments')
        updated_review.user_id = user_id
        updated_review.phone = data.get('review-update-form-booking-phone-checkbox')
        updated_review.online = data.get('review-update-form-booking-online-checkbox')
        updated_review.walkin = data.get('review-update-form-booking-walkin-checkbox')

        db.session.commit()

        message = Markup('Review updated successfully!<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
        flash(message, 'success')

        return redirect(url_for('reviews'))

    current_review = Review.query.get(review_id)
    vibes = Vibe.query.all()

    return render_template(
        'review-update.html', review=current_review, vibes=vibes)


# route to delete a review
@app.route('/review_delete/<review_id>')
def review_delete(review_id):

    review_to_be_deleted = db.session.query(Review).filter(Review.id == review_id).first()
    db.session.delete(review_to_be_deleted)
    db.session.commit()

    message = Markup('Review deleted successfully!<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
    flash(message, 'success')

    return redirect(url_for('reviews'))


# route to contact site owner
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
