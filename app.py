import os
from flask import (
    Flask, flash, render_template, request, url_for,
    redirect, session, Markup)
# for password hashing
from werkzeug.security import (
    generate_password_hash, check_password_hash)
from flask_sqlalchemy import SQLAlchemy
from models import User, Review, Vibe
from sqlalchemy import create_engine
import smtplib
from email.message import EmailMessage
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

# SQLAlchemy engine configuration (with connection pooling)
DATABASE_CONNECTION = os.environ.get(
    'SQLALCHEMY_DATABASE_URI')
engine = create_engine(DATABASE_CONNECTION, pool_size=50, max_overflow=100)

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
            message = Markup(
                'Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(firstname) > 0 and len(firstname) < 2:
            message = Markup(
                'Your first name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(firstname) > 50:
            message = Markup(
                'Your first name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(lastname) > 0 and len(lastname) < 2:
            message = Markup(
                'Your last name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(lastname) > 50:
            message = Markup(
                'Your last name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 0 and len(email) < 6:
            message = Markup(
                'Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 100:
            message = Markup(
                'Your email address is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) > 0 and len(password2) > 0 and len(password1) < 8 or len(password2) < 8:
            message = Markup(
                'Your password is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) > 100 or len(password2) > 100:
            message = Markup(
                'Your password is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(password1) >= 8 and len(password2) >= 8 and len(password1) < 100 and len(password2) < 100 and password1 != password2:
            message = Markup(
                'Your passwords don\'t match!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

        if len(firstname) >= 2 and len(firstname) <= 50 and len(lastname) >= 2 and len(lastname) <= 50 and len(email) >= 6 and len(email) <= 100 and len(password1) >= 8 and len(password2) >= 8 and len(password1) <= 100 and len(password2) <= 100 and password1 == password2:
            # Check to see if user/email entered already exists in DB
            if db.session.query(User).filter(User.email == email).count() == 0:
                # flash msg here to confirm user registration upon redirect
                message = Markup(
                    'Thanks for registering, {} <i class="fas fa-cut"></i></br>Welcome to the Clipadvisor community!</br>Is there a new barber you\'d like to tell us about?'.format(firstname))
                flash(message, 'success')

                new_user = User(
                    firstname=firstname, lastname=lastname, email=email, password=generate_password_hash(
                        password1, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                db.session.close()

                # Store newly-registered user in session cookie
                session['user'] = data.get('register-form-email')

                return redirect(url_for('review_submit'))

            message = Markup(
                'There is already an account associated with that email! Please try again <i class="fas fa-cut"></i>')
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
            message = Markup(
                'Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(email) > 0 and len(email) < 6:
            message = Markup(
                'Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(email) > 100:
            message = Markup(
                'Your email address is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

        if len(email) >= 6 and len(email) <= 100 and len(password) >= 8 and len(password) <= 100:
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
                        message = Markup(
                            'You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
                        flash(message, 'warning')
            else:
                # Another deliberately ambiguous message to guard against malicious brute-force login attempts
                message = Markup(
                    'You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
                flash(message, 'warning')

        else:
            # Another deliberately ambiguous message to guard against malicious brute-force login attempts
            message = Markup(
                'You have entered an invalid email address/password!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

    return render_template('login.html')


# route to log user out
@app.route('/logout')
def logout():

    user = User.query.filter_by(email=session['user']).first()

    # Remove/Destroy session cookie associated with user
    session.pop('user')

    return render_template('logout.html', user=user)


# route to view all barbers
@app.route('/barbers')
def barbers():
    # barbers displayed in alphabetical order
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.order_by(
        Review.barbershopname.asc()).paginate(page=page, per_page=10)
    return render_template('barbers.html', reviews=reviews)


# route to view top-rated barbers
@app.route('/barbers-top')
def top_barbers():
    # barbers displayed in alphabetical order
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(rating=5)\
        .order_by(Review.barbershopname.asc())\
        .paginate(page=page, per_page=10)
    return render_template('barbers-top.html', reviews=reviews)


# route to view walk-in barbers
@app.route('/barbers-walkin')
def walkin_barbers():
    # barbers displayed in alphabetical order
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(walkin='walk-in')\
        .order_by(Review.barbershopname.asc())\
        .paginate(page=page, per_page=10)
    return render_template('barbers-walkin.html', reviews=reviews)


# route to view cash-friendly barbers
@app.route('/barbers-cash')
def cash_barbers():
    # barbers displayed in alphabetical order
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(cash='cash')\
        .order_by(Review.barbershopname.asc())\
        .paginate(page=page, per_page=10)
    return render_template('barbers-cash.html', reviews=reviews)


# route to view barbers filtered by vibe
@app.route('/_barbers/<string:vibe>')
def _barbers(vibe):
    vibe = Vibe.query.filter_by(vibe_name=vibe).first_or_404()
    # barbers displayed in alphabetical order
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(vibe=vibe.vibe_name)\
        .order_by(Review.barbershopname.asc())\
        .paginate(page=page, per_page=10)
    return render_template('_barbers.html', reviews=reviews, vibe=vibe)


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
        if customername == '' or barbershopname == '' or date == '' or time == '' or phone == '' and online == '' and walkin == '' or cash == '' and card == '' or vibe == '' or comments == '' or rating == '':
            message = Markup(
                'Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(customername) > 0 and len(customername) < 4:
            message = Markup(
                'Your name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(customername) > 50:
            message = Markup(
                'Your name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(barbershopname) > 0 and len(barbershopname) < 3:
            message = Markup(
                'Your barber\'s name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(barbershopname) > 50:
            message = Markup(
                'Your barber\'s name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(comments) > 0 and len(comments) < 10:
            message = Markup(
                'Your comment is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(comments) > 1000:
            message = Markup(
                'Your comment is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

        if len(customername) >= 4 and len(customername) <= 50 and len(barbershopname) >= 3 and len(barbershopname) <= 50 and date != '' and time != '' and len(comments) >= 10 and len(comments) <= 1000 and rating != '':
            # flash msg here to confirm review submission upon redirect
            message = Markup(
                'Thanks for rating your barber!<br>Your name will be entered into a draw at the end of the month to win a €100 barbershop voucher.<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
            flash(message, 'success')

            new_review = Review(
                customername=customername, barbershopname=barbershopname, date=date, time=time, cash=cash, card=card, vibe=vibe, rating=rating, comments=comments, user_id=user_id, phone=phone, online=online, walkin=walkin)
            db.session.add(new_review)
            db.session.commit()
            db.session.close()

            return redirect(url_for('reviews'))

    return render_template(
        'review-submit.html', user=user)


# route to update a review
@app.route('/review-update/<review_id>', methods=['GET', 'POST'])
def review_update(review_id):

    user = User.query.filter_by(email=session['user']).first()
    current_review = Review.query.get(review_id)

    if request.method == 'POST':

        data = request.form
        updated_review = db.session.query(
            Review).filter(Review.id == review_id).first()
        updated_review.customername = data.get(
            'review-update-form-customer-name')
        updated_review.barbershopname = data.get(
            'review-update-form-barbershop-name')
        updated_review.date = data.get('review-update-form-date-picker')
        updated_review.time = data.get('review-update-form-time-picker')
        updated_review.cash = data.get(
            'review-update-form-payment-cash-checkbox')
        updated_review.card = data.get(
            'review-update-form-payment-card-checkbox')
        updated_review.vibe = data.get('review-update-form-vibe')
        updated_review.rating = data.get('review-update-form-star-rating')
        updated_review.comments = data.get('review-update-form-comments')
        updated_review.user_id = current_review.user_id
        updated_review.phone = data.get(
            'review-update-form-booking-phone-checkbox')
        updated_review.online = data.get(
            'review-update-form-booking-online-checkbox')
        updated_review.walkin = data.get(
            'review-update-form-booking-walkin-checkbox')

        # Update Review form validation and categorised flash messaging conditional logic
        if updated_review.customername == '' or updated_review.barbershopname == '' or updated_review.date == '' or updated_review.time == '' or updated_review.phone == '' and updated_review.online == '' and updated_review.walkin == '' or updated_review.cash == '' and updated_review.card == '' or updated_review.vibe == '' or updated_review.comments == '' or updated_review.rating == '':
            message = Markup(
                'Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(
            updated_review.customername) > 0 and len(
                updated_review.customername) < 4:
            message = Markup(
                'Your name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(updated_review.customername) > 50:
            message = Markup(
                'Your name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(updated_review.barbershopname) > 0 and len(updated_review.barbershopname) < 3:
            message = Markup(
                'Your barber\'s name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(updated_review.barbershopname) > 50:
            message = Markup(
                'Your barber\'s name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(updated_review.comments) > 0 and len(updated_review.comments) < 10:
            message = Markup(
                'Your comment is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(updated_review.comments) > 1000:
            message = Markup(
                'Your comment is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')

        if len(updated_review.customername) >= 4 and len(updated_review.customername) <= 50 and len(updated_review.barbershopname) >= 3 and len(updated_review.barbershopname) <= 50 and updated_review.date != '' and updated_review.time != '' and len(updated_review.comments) >= 10 and len(updated_review.comments) <= 1000 and updated_review.rating != '':

            db.session.commit()
            db.session.close()

            # flash msg here to confirm review resubmission upon redirect
            message = Markup(
                'Review updated successfully!<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
            flash(message, 'success')

            return redirect(url_for('reviews'))

    vibes = Vibe.query.all()

    if current_review.user_id == user.id or user.id == 257:
        return render_template(
            'review-update.html', review=current_review, vibes=vibes)


# route to view all reviews as visiting user
@app.route('/reviews_')
def reviews_():
    # reviews displayed in descending order of recency (
    # i.e. most recent reviews first)
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.order_by(
        Review.id.desc()).paginate(page=page, per_page=10)
    return render_template('reviews.html', reviews=reviews)


# route to view all reviews as logged-in user
@app.route('/reviews')
def reviews():
    current_user = User.query.filter_by(email=session['user']).first()
    # reviews displayed in descending order of recency (
    # i.e. most recent reviews first)
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.order_by(
        Review.id.desc()).paginate(page=page, per_page=10)
    return render_template('reviews.html', user=current_user, reviews=reviews)


# route to view all reviews as logged-in user
@app.route('/my-reviews')
def my_reviews():
    current_user = User.query.filter_by(email=session['user']).first()
    # reviews displayed in descending order of recency (
    # i.e. most recent reviews first)
    page = request.args.get('page', 1, type=int)
    reviews = Review.query.filter_by(user_id=current_user.id)\
        .order_by(Review.id.desc())\
        .paginate(page=page, per_page=10)
    return render_template(
        'my-reviews.html', user=current_user, reviews=reviews)


# route to delete a review
@app.route('/review_delete/<review_id>')
def review_delete(review_id):

    review_to_be_deleted = db.session.query(
        Review).filter(Review.id == review_id).first()
    db.session.delete(review_to_be_deleted)
    db.session.commit()
    db.session.close()

    message = Markup(
        'Review deleted successfully!<br><i class="fas thanks-for-reviewing-icon fa-cut pt-1"></i>')
    flash(message, 'success')

    return redirect(url_for('reviews'))


# route to contact site owner
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    EMAIL_ADDRESS = os.environ.get('EMAIL_USERNAME')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    if request.method == 'POST':
        msg = EmailMessage()
        data = request.form
        sender_name = data.get('contact-form-name')
        sender_email = data.get('contact-form-email')
        category = data.get('contact-form-category')
        sender_message = data.get('contact-form-message')

        # Contact form validation and categorised flash messaging conditional\
        #  logic
        if sender_name == '' or sender_email == '' or category == '' or sender_message == '':
            message = Markup(
                'Please fill out all fields!<br><i class="fas all-fields-icon fa-cut pt-1"></i>')
            flash(message, 'warning')
        if len(sender_name) > 0 and len(sender_name) < 4:
            message = Markup(
                'Your name is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(sender_name) > 50:
            message = Markup(
                'Your name is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(sender_email) > 0 and len(sender_email) < 6:
            message = Markup(
                'Your email address is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(sender_email) > 50:
            message = Markup(
                'Your email address is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(sender_message) > 0 and len(sender_message) < 10:
            message = Markup(
                'Your message is too short!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(sender_message) > 2000:
            message = Markup(
                'Your message is too long!</br>Please try again <i class="fas fa-cut"></i>')
            flash(message, 'warning')
        if len(sender_name) >= 4 and len(sender_name) <= 50 and len(sender_email) >= 6 and len(sender_email) <= 50 and category != '' and len(sender_message) >= 10 and len(sender_message) <= 2000:
            msg['Subject'] = 'You have a new message from a Clipadvisor user!'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = 'hello@loosenthedark.tech'
            msg.set_content('This is a plain text email')
            msg.add_alternative(
                f"<ul><li><strong>Message category:</strong> {category}</li><li><strong>Message:</strong> {sender_message}</li><li><strong>Message sender:</strong> {sender_name}</li><li><strong>Sender's email:</strong> {sender_email}</li></ul><br>&#128513;", subtype='html')
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                smtp.send_message(msg)

            return redirect(url_for('thank_you'))

    return render_template('contact.html')


# route to thank user for submitting contact form
@app.route('/thank-you')
def thank_you():

    return render_template('thank-you.html')


# Custom error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html'), 403


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500


# conditional check to see whether the app is being run directly or as an
# import
# ---> if it's the former, the app will be launched
if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP'), port=5000)
