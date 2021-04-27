<h1 align='center'>Clipadvisor Web Application</h1>



<p align="center"><img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" alt="Code Institute logo" width="200" height="auto"></p>
<p align="center"><img src="docs/images/screenshots/clipadvisor-logo.png" alt="Clipadvisor logo" width="200" height="auto"></p>



<p align="center" style="font-style:italic;">Code Institute Diploma in Software Development: Python and Data-Centric Development - Milestone Project</p>



<p align="center"><a href="https://clipadvisor-flask-app.herokuapp.com/" style="font-weight:bold;">Live link to deployed project</a> (hosted on Heroku)</p>



---



**Clipadvisor** is a full-stack web application that boasts comprehensive CRUD functionality, allowing users to post, view, edit and delete reviews of barbers. Backend data processing is facilitated by Python+Flask in tandem with SQLAlchemy (via the Flask-SQLAlchemy extension). Dynamic templating logic has been put in place to enable visitors to navigate with ease and choose from an appropriate selection of frontend pages (routes), depending on whether they are logged in or out. The site offers a highly rewarding User Experience through the use of carefully-targetted colour schemes, fully-responsive design flourishes and smart interactivity. Overall, it comfortably fulfills its goal of being "a cut above" its competitors!



<p align="center"><img src="docs/images/screenshots/clipadvisor-landing.png" alt="Clipadvisor landing (Home) page screenshots across multiple device sizes" width="70%" height="auto"></p>



## User Experience (UX)

As we emerge from Level-5 lockdown, and normality slowly returns to the services and retail sectors, the majority of us will be looking forward to getting a long-overdue and much-needed haircut. Given that this set of circumstances will likely result in long waiting lists at barbers everywhere, it would be nice to know which businesses are worth waiting in line for and which should best be avoided.

That's where Clipadvisor comes in, offering users a convenient, trustworthy and authoritative source of barbershop ratings and reviews.

As with any such application, the best way to showcase Clipadvisor's benefits and features is to profile a number of **User Stories** pertaining to typical visitors to the site. With this in mind, a list of such User Stories might include (but by no means be limited to) the following:

1. "As a first-time user, I would like to be able to CREATE a review of a barber I visited recently."
2. "As a first-time user, I would like to be able to READ reviews of barbers posted previously by others."
3. "As a first-time user, I would like to be able to search for a review(s) of a particular barber I am thinking of visiting."
4. "As a returning user, I would like to be able to UPDATE a review I posted recently."
5. "As a returning user, I would like to be able to DELETE a review I posted recently."
6. "As a Clipadvisor user, I would like to be able to contact the site owner(s) with a query/feature request."
7. "As a developer, I would like to be able to contact the site owner(s) to offer feedback on the app's functionality."
8. "As site owner, I would like to be able to moderate all user-submitted content, i.e. have the ability to UPDATE and/or DELETE reviews where necessary."
9. "As site owner, I would like for users to be able to contact me directly, i.e. without having to leave the application."



On the **Design** front, a [Material Design for Bootstrap](https://mdbootstrap.com/) stylesheet was used to give the site its overall look and feel - more specifically, the [MDB jQuery 3 (default Bootstrap 4 version)](https://mdbootstrap.com/docs/b4/jquery/) was chosen for this purpose.



The traditional 'barbers pole' **colours** of red, blue and white are employed throughout. The particular shades of red and blue (given the class names `.barber-red` and `.barber-blue`, respectively, in the site's custom stylesheet) are taken from [this Shutterstock 'barber shop icon'](https://www.shutterstock.com/image-vector/barber-symbol-shop-icon-hair-service-1070505362?id=1070505362&irclickid=1jiSOcU5OxyLUmQwUx0Mo3EqUkEXh30ItXjY1M0&irgwc=1&utm_medium=Affiliate&utm_campaign=Free%20SVG&utm_source=2022575&utm_term=&c3ch=Affiliate&c3nid=IR-2022575), and lend visual clarity and consistency to the site.



In terms of **font** preferences, things were kept pretty simple: Roboto was chosen for the vast majority of site text; this is complemented by [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed?query=roboto+conde) for most headings, as well as for the `.navbar-brand` Clipadvisor logo element.



From the perspective of **imagery**, the site's background hero image (a hand-drawn sketch featuring a variety of barbershop utensils) is a stock illustration [taken from Shutterstock's library](https://www.shutterstock.com/image-illustration/barber-shop-seamless-pattern-hand-drawn-1715625478). The aforementioned ['barbers pole' icon](https://www.shutterstock.com/image-vector/barber-symbol-shop-icon-hair-service-1070505362?id=1070505362&irclickid=1jiSOcU5OxyLUmQwUx0Mo3EqUkEXh30ItXjY1M0&irgwc=1&utm_medium=Affiliate&utm_campaign=Free%20SVG&utm_source=2022575&utm_term=&c3ch=Affiliate&c3nid=IR-2022575), used for the site's favicon as well as to accompany most of the main headings, is also used with permission from Shutterstock. All other icons are imported from [Font Awesome](https://fontawesome.com/), and are used here in accordance with [their licence](https://fontawesome.com/license).



All pre-existing site content (user profiles, barbershop names, reviews etc.) at the time of writing is purely generic filler text compiled by the site's creator for the sake of authenticity.



## Features

### Existing Features:

#### Navigation

- The site boasts a dynamically-populated `.navbar` (collapsed on mobile devices) that is displayed across the top of each page and responds to whether the user happens to be logged in or not at any given time:
<p align="center"><img src="docs/images/screenshots/clipadvisor-navbar-logged-out1.png" alt="Clipadvisor logged-out user navbar on mobile" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-navbar-logged-out2.png" alt="Clipadvisor logged-out user navbar on tablet" width="25%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-navbar-logged-in1.png" alt="Clipadvisor logged-in user navbar on mobile" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-navbar-logged-in2.png" alt="Clipadvisor logged-in user navbar on tablet" width="25%" height="auto"></p>


#### Main landing (Home) page:

- Visitors are greeted by an eye-catching `.jumbotron` message encouraging them to contribute a review by clicking on the blue and white 'call-to-action' `button`:

<p align="center"><img src="docs/images/screenshots/clipadvisor-landing1.png" alt="Clipadvisor landing page call-to-action" width="15%" height="auto"></p>

- Assuming that the user _is not_ already logged-in, clicking on this `button` will bring them to the site's registration page. Here, they can either:
  - fill out and submit a short form in order to create a profile (a requirement for posting reviews)
  or...
  - click instead on the login `button` beneath the registration form, which will bring them to the login page where they can enter their previously-registered email and password in order to log in
  - In either case, they will then be redirected to a page where they can compose and submit a review (a dismissible Flash welcome message - styled using Bootstrap's `.alert` classes - will appear between the main `.navbar` and the 'Rate your barber!' heading at the top of the `form` when they first arrive on this `/review-submit` page):
<p align="center"><img src="docs/images/screenshots/clipadvisor-register-pre.png" alt="Clipadvisor registration form" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-register-post.png" alt="Clipadvisor review submit form post-registration" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-login-pre.png" alt="Clipadvisor login form" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-login-post.png" alt="Clipadvisor review submit form post-login" width="15%" height="auto"></p>

- If, on the other hand, the user _is_ already logged-in, then clicking on the landing page's CTA `button` will take them directly to this review submission form (minus any Flash messaging, as this is seen as being redundant here):
<p align="center"><img src="docs/images/screenshots/clipadvisor-landing-logged-in1.png" alt="Clipadvisor landing page for logged-in user" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-landing-logged-in2.png" alt="Clipadvisor review submit form for logged-in user" width="15%" height="auto"></p>

#### Login/Registration page

- The login link in the site's main `.navbar` simply brings the user to the login page illustrated above. If they're not already registered at this point, they will have to do so by leaving the login page via the 'Register Here' button at the foot of the login form. This will redirect them to the registration form, where they can enter their details (as with all forms across the site, all `input` fields here are required)
<p align="center"><img src="docs/images/screenshots/clipadvisor-login-form.png" alt="Clipadvisor login form" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-registration-form.png" alt="Clipadvisor registration form" width="15%" height="auto"></p>

#### Barbers page(s)

- The Barbers link in the main `.navbar` leads the user to four interconnected pages, each of which applies a different filter to the list of barbers stored in the app's backend database:
<p align="center"><img src="docs/images/screenshots/clipadvisor-barbers.png" alt="Clipadvisor Barbers page screenshots across multiple device sizes" width="70%" height="auto"></p>
  
- A compact tabbed interface has been put in place using Bootstrap's `.nav-tabs` class for streamlined sorting of all stored barbershops under a variety of self-explanatory headings:
  - 'All Barbers'
  - 'Top-Rated'
  - 'Walk-Ins Welcome'
  - 'Cash Accepted'

<p align="center"><img src="docs/images/screenshots/clipadvisor-barbers-nav-tabs1.png" alt="Clipadvisor Barbers page tabbed navbar UI" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-barbers-nav-tabs2.png" alt="Clipadvisor Barbers page tabbed navbar UI" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-barbers-nav-tabs3.png" alt="Clipadvisor Barbers page tabbed navbar UI" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-barbers-nav-tabs4.png" alt="Clipadvisor Barbers page tabbed navbar UI" width="15%" height="auto"></p>

- This is intended to enhance the overall UX by providing (relatively basic) search functionality, in lieu of an actual site-wide search bar (a potential future feature to be added at a later date)

- In addition to this tabbed sorting, a visually-appealing colour scheme has also been applied to the alphabetised list of barbers displayed based on user descriptions: all "cheap & cheerful" barbers are thus given a light green `.card-header` element (etc.)

- Furthermore, when a user clicks on one of these descriptor tags (e.g. 'cheap & cheerful') within the `.card-body` they are brought to a list comprised solely of barbers with that same 'vibe':

<p align="center"><img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-1.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-2.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-3.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-4.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-5.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-6.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-7.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto" style="margin-right: 0.5%;">
<img src="docs/images/screenshots/clipadvisor-barbers-vibes-pages-8.png" alt="Clipadvisor Barbers categorised pages" width="12%" height="auto"></p>

#### Recent Reviews page

- The Recent Reviews link in the main `.navbar` brings the user to a list of reviews filtered by recency (with the most recent reviews at the top of this list)
- The colour scheme is the same for all reviews this time, however:
<p align="center"><img src="docs/images/screenshots/clipadvisor-recent-reviews1.png" alt="Clipadvisor Recent Reviews page screenshot on tablet" width="25%" height="auto"></p>

- Clicking on the 'More Info' `button` embedded within the body of each review triggers an informational `.modal` component giving a breakdown of some of the more granular aspects of each barbershop experience:
<p align="center"><img src="docs/images/screenshots/clipadvisor-recent-reviews2.png" alt="Clipadvisor Recent Reviews page 'More Info' modal screenshot on tablet" width="25%" height="auto"></p>

- Logged-in users will notice that reviews they have previously submitted are displayed in bolder colours that make them stand out
- They will also see two additional buttons attached to each of their submitted reviews allowing them to either **update** or **delete** the review in question (see User Stories for a more thorough exploration of this CRUD functionality)
<p align="center"><img src="docs/images/screenshots/clipadvisor-recent-reviews3.png" alt="Clipadvisor Recent Reviews page logged-in user UI screenshot on desktop" width="60%" height="auto"></p>

- As with the Barbers page(s) discussed above, pagination has been implemented at the foot of the Recent Reviews UI. The number of reviews displayed per page is capped at ten. Users can navigate both backwards and forwards using custom pagination links.
<p align="center"><img src="docs/images/screenshots/clipadvisor-pagination-1.png" alt="Clipadvisor custom pagination links" width="15%" height="auto" style="margin-right: 1%;">
<img src="docs/images/screenshots/clipadvisor-pagination-2.png" alt="Clipadvisor custom pagination links" width="15%" height="auto" style="margin-right: 1%;">
<img src="docs/images/screenshots/clipadvisor-pagination-3.png" alt="Clipadvisor custom pagination links" width="15%" height="auto" style="margin-right: 1%;">
<img src="docs/images/screenshots/clipadvisor-pagination-4.png" alt="Clipadvisor custom pagination links" width="15%" height="auto" style="margin-right: 1%;">
<img src="docs/images/screenshots/clipadvisor-pagination-5.png" alt="Clipadvisor custom pagination links" width="15%" height="auto" style="margin-right: 1%;">
<img src="docs/images/screenshots/clipadvisor-pagination-6.png" alt="Clipadvisor custom pagination links" width="15%" height="auto"></p>

- This pagination functionality was built with help from [this YouTube tutorial](https://www.youtube.com/watch?v=PSWf2TjTGNY)

#### Submit A Review page

- Once a user is logged in (see above), they may post a review to the site by completing a `form` element consisting of a total of nine `.form-group` input fields and a submit button. All nine of these fields are required (in the case of both the 'booking options' and 'payment options' fields, a minimum of one checkbox must be selected). A combination of browser-default HTML5 `form` validation and both custom client-side and server-side validation prevents users from submitting incomplete forms.
<p align="center"><img src="docs/images/screenshots/clipadvisor-review-submit-form.png" alt="Clipadvisor review submit form screenshot on tablet" width="25%" height="auto"></p>

- When they have successfully completed and submitted this form, the user is redirected to the Recent Reviews page (see above), where they will see their posted review at the top of the page. There will also be a dismissible Flash messaging alert box right below the main `.navbar` thanking them for contributing to Clipadvisor.
<p align="center"><img src="docs/images/screenshots/clipadvisor-review-submit-post-submit-redirect.png" alt="Clipadvisor review submit form post-submission redirect screenshot on tablet" width="25%" height="auto"></p>

#### My Reviews page

- A logged-in user can find all of their submitted reviews together in one place by clicking on the 'My Reviews' link in the main `.navbar`. Much like its parent 'Recent Reviews' page, this personalised page displays the user's reviews in reverse chronological order (most recent reviews at the top). The user can also avail of full update and delete functionality here by using the corresponding buttons (as outlined above):
<p align="center"><img src="docs/images/screenshots/clipadvisor-my-reviews.png" alt="Clipadvisor My Reviews page screenshot on tablet" width="25%" height="auto"></p>

#### Contact page

- It's easy for users to contact the site owner, regardless of whether they happen to be logged-in regular visitors or first-time guests. Selecting the Contact link in the main `.navbar` brings them to a user-friendly contact form, where they are asked to fill in the details of their request/query/feedback. If the user _is_ logged in at this point, they are not asked to provide their email address, as this will already be stored in the current session's cookie data. Logged-out users, on the other hand, will have to provide an email address in order to submit the contact form (whose `input` fields are once again all required).

- Assuming everything is in order and all `form` fields have been completed, the user is briefly redirected to a page thanking them for getting in touch and assuring them that someone from Clipadvisor will respond to their request/query/feedback in due course. A simple JavaScript timeout function has been set on this page which then returns the user to the site's Home page after five seconds.
<p align="center"><img src="docs/images/screenshots/clipadvisor-contact-logged-in-user.png" alt="Clipadvisor Contact page logged-in user form view" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-contact-logged-out-user.png" alt="Clipadvisor Contact page logged-out user form view" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-contact-post-redirect1.png" alt="Clipadvisor Contact page post-submit redirect page" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-contact-post-redirect2.png" alt="Clipadvisor Contact page post-submit redirect back to Home page" width="15%" height="auto"></p>

#### Logging out

- Logged-in users can log out of the site at any time by clicking the Log Out link in the main `.navbar`. In a similar vein as the post-submission redirect functionality applied to the Contact page, as soon as a user logs out they are briefly taken to a holding screen where their logout is confirmed and they are thanked for being a part of Clipadvisor. This is swiftly followed (again, after five seconds) by a second redirect that returns them to the site's Home page.
<p align="center"><img src="docs/images/screenshots/clipadvisor-logout-1.png" alt="Clipadvisor logout functionality step 1" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-logout-2.png" alt="Clipadvisor logout functionality step 2" width="15%" height="auto" style="margin-right: 20px;">
<img src="docs/images/screenshots/clipadvisor-logout-3.png" alt="Clipadvisor logout functionality step 3" width="15%" height="auto"></p>

#### Wireframes

- [mobile](docs/wireframes/clipadvisor_mobile.pdf)
- [tablet](docs/wireframes/clipadvisor_tablet.pdf)
- [desktop](docs/wireframes/clipadvisor_desktop.pdf)

### Potential Future Features

- Enhanced user submission functionality, e.g. a way for reviewers to upload a picture(s) of the barbers premises/the haircut they received when submitting/updating a review
- A way to attach an accurate timestamp to each review as it's submitted, and possibly display this alongside the date of the visit in question
- Making upvoting/downvoting of reviews available to logged-in users
- Increased security features:
  - Email confirmation/validation during registration
  - Two-Factor Authentication (2FA) during login
  - Requiring users to solve a CAPTCHA when submitting/updating a review
  - Verification of all reviews, e.g. by requiring users to upload a copy of their receipt when submitting a review
  - Ability to ban or restrict certain IP address(es) from accessing the app in response to suspicious or malicious activity
- Password reset functionality to cater for users forgetting their passwords
- A means for registered users to log in via a linked social media account(s)
- "Email me a copy of my review/query/feedback" (optional) checkbox functionality attached to each of the site's `form`s
- A site-wide search bar
- Enabling users to provide (optional?) location and/or contact info for barbers, e.g. by leveraging the Google Maps API or something similar
- Ultimately, a way to make Clipadvisor a 'one-stop shop' for both customers and business owners, with full booking functionality and regular features like competition giveaways, social media promotions and product tie-ins.



## Technologies Used

### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python 3](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries, Programmes, Toolkits & Engines

- [Bootstrap](https://getbootstrap.com/) [(v4.5.0)](https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.0/js/bootstrap.min.js)
- [Material Design for Bootstrap 4](https://mdbootstrap.com/docs/b4/jquery/) [v4.19.1](https://cdnjs.com/libraries/mdbootstrap/4.19.1)
- [jQuery](https://jquery.com/) [(v3.5.1)](https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Popper.js](https://popper.js.org/)
- [jQuery DateTimePicker plugin](https://xdsoft.net/jqplugins/datetimepicker/)
- [Flask](https://palletsprojects.com/p/flask/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Jinja](https://palletsprojects.com/p/jinja/)



## Testing

Full application testing details can be found [here](testing.md)



## Database

- To get started, [the following steps were followed using Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#quickstart):
  1. Create the Flask application
  2. Load all relevant configuration variables (from a local `env.py` file)
  3. Create the SQLAlchemy object by passing it the application

<p align="center"><img src="docs/images/screenshots/clipadvisor-database-start-screenshot.png" alt="Clipadvisor database initiation steps screenshot" width="30%" height="auto"></p>

- From there, the `Model` class provided by this object was used as a declarative base for [declaring models (in the `models.py` file)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/), with an `__init__` method defined on all subsequent model classes
- The table name for each class was also set using the optional `__tablename__` class attribute

<p align="center"><img src="docs/images/screenshots/clipadvisor-database-declaring-models-screenshot.png" alt="Clipadvisor database declaring models screenshot" width="30%" height="auto"></p>

- As illustrated above, the app's CRUD functionality allows for full user interaction with the database, which was implemented by calling each of the following at the appropriate junctures (e.g. when a new user registers succuessfully), always remembering to commit the session afterwards:

<p align="center"><img src="docs/images/screenshots/clipadvisor-database-session-crud-screenshot.png" alt="Clipadvisor database declaring models screenshot" width="30%" height="auto"></p>

- Finally, [these steps](https://www.postgresqltutorial.com/postgresql-create-table/) were executed from the command line to create Heroku Postgres (PostgreSQL) tables with the data obtained from Clipadvisor users



## <a name="deployment"></a>Deployment

A development version of this project was hosted on [**GitHub**](https://github.com/), with [**Gitpod**](https://gitpod.io/workspaces) as the chosen IDE. At the time of writing it has only one (master) branch.

In order to run this project locally, you can clone [the remote GH repository](https://github.com/loosenthedark/clipadvisor-flask-app) for use and modification within your own local environment. This can easily be done by first of all changing the current working directory in your Terminal to the location where you want the cloned directory to be created. Once this is done, simply type "git clone https://github.com/loosenthedark/clipadvisor-flask-app.git" into the command line. A more thorough explanation of all the steps involved in this cloning process can be found [here](https://help.github.com/en/articles/cloning-a-repository).

The project is deployed on [**Heroku**](https://dashboard.heroku.com/apps), and can be accessed using the following URL: https://clipadvisor-flask-app.herokuapp.com/

The steps involved in deployment were as follows:

1. Create `requirements.txt` file

  ```
  pip3 freeze > requirements.txt
  ```

2. Create `Procfile`

  ```
  echo web: gunicorn app:app > Procfile
  ```

3. Create `runtime.txt` file

  ```
  echo python-3.8.8 > runtime.txt
  ```

4. [Log in to Heroku](https://id.heroku.com/login) and click on **clipadvisor-flask-app** from the list of created apps

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku1.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

5. Go to 'Settings'

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku2.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

6. Click the **Reveal Config Vars** button in the 'Config Vars' section

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku3.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

7. Copy all relevant configuration variables required to run the application from the development version's `env.py` file and paste them in here as key-value pairs

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku4.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

8. Go to 'Resources'

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku5.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

9. In the 'Add-ons' search bar, search for and select **Heroku Postgres** (making sure to choose 'Hobby Dev - Free' as the plan name) by clicking on the **Submit Order Form** button to add it to the app

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku6.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>
<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku7.png" alt="Clipadvisor Heroku deployment steps screenshot" width="20%" height="auto"></p>

10. Go to 'Deploy'

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku8.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

11. Select **GitHub** in the 'Deployment method' section

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku9.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

12. Ensure that the project's master branch is selected under 'Deploy a GitHub branch' in the 'Manual deploy' section

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku10.png" alt="Clipadvisor Heroku deployment steps screenshot" width="70%" height="auto"></p>

13. After clicking on the **Deploy Branch** button, you should see a message confirming that "Your app was successfully deployed" followed by a **View** button which can be clicked to launch and view the app

<p align="center"><img src="docs/images/screenshots/clipadvisor-deployment-heroku11.png" alt="Clipadvisor Heroku deployment steps screenshot" width="50%" height="auto"></p>



## Credits

### Code

- The following articles and resources proved helpful at various stages throughout the project's evolution:

  - ['Flask CRUD Application with SQLAlchemy'](https://codeloop.org/flask-crud-application-with-sqlalchemy/) (Parwiz Forogh at CodeLoop)

  - ['Python Website Full Tutorial - Flask, Authentication, Databases & More'](https://www.youtube.com/watch?v=dam0GPOAvVI) (Tech With Tim on YouTube)

  - An auto-generated 'secret key' password used in the app's configuration was created by [this online key-gen tool](https://passwordsgenerator.net/)
  
  - A way of disabling 'false positive' error messages thrown by [Pylint](https://pypi.org/project/pylint/) in relation to the `scoped_session` class ("instance of scoped_session has no add/commit member" etc.) was [found here](https://stackoverflow.com/questions/59214324/flask-error-db-scoped-session-instance-of-scoped-session-has-no-commit-mem)

  - The bespoke 'page rating' code snippet used within the site's `#review-submit-form` and `#review-update-form` was adapted from [this template](https://codepen.io/hesguru/pen/BaybqXv)

  - The Material Design 'block' components used across the 'Barbers', 'Recent Reviews' and 'My Reviews' pages have been adapted from [Marta Wierzbicka's original design](https://mdbootstrap.com/snippets/jquery/marta-szymanska/1343674)

  - Users are required to specify at least one available booking option and one available payment option when submitting/updating a review by means of a [jQuery validation script that has been used with permission](https://www.howtocodeschool.com/2019/11/submit-form-If-at-least-one-checkbox-is-checked.html)

  - The repository housing the source code for the jQuery DateTimePicker plugin used in the `#review-submit-form` and `#review-update-form` can be found [here](https://github.com/xdan/datetimepicker)

  - After trying everything including chatting with Igor on the Code Institute Tutor Assistance tab, and even going as far as creating a brand new workspace, uninstalling and then reinstalling all of the package dependencies from my `requirements.txt` file (none of which resolved the issue), I finally discovered that the cause of a persistent `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres` error was a bug linked to how SQLAlchemy stores the dialect for the project's Database URI (environment variable). After following the advice [on this forum](https://github.com/pallets/flask-sqlalchemy/issues/929), I was eventually able to overcome this problem by modifying the DB URI dialect in my `env.py` file

  - I was able to make Flash messages more visually appealing by adding some basic markup (for line breaks etc.) using the [`flask.Markup` extension](https://tedboy.github.io/flask/generated/generated/flask.Markup.html) after following advice posted on [this Stack Overflow thread](https://stackoverflow.com/questions/18225713/how-to-display-html-content-through-flask-messages)

  - Dynamic-width Flash message alert functionality was implemented with help from [this Stack Overflow response](https://stackoverflow.com/questions/31721816/set-divs-width-equal-to-another-div) (and augmented by [alert resize on screen resize](https://api.jquery.com/resize/))

  - I got some help with using the appropriate Jinja syntax to display user reviews in descending order of recency (i.e. sorting the list returned from my database by id in reverse order) from [this Stack Overflow thread](https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2)

  - On desktop devices, I wanted a way to display two barbers/reviews per row so as to take advantage of the increased screen width. I was able to achieve this objective using the [batch filter](https://jinja.palletsprojects.com/en/2.11.x/templates/#batch) thanks to the top answer to [this Stack Overflow query](https://stackoverflow.com/questions/17797921/jinja2-create-new-row-for-every-3-items)

  - I received pointers for generating email in Python from contact form user input from [this Corey Schafer video tutorial](https://www.youtube.com/watch?v=JRCJ6RtE3xU)
  
  - Lastly, several code blocks used in the [Deployment section of this Markdown file](#deployment) have been beautified with the free-to-use [Ray.so](https://ray.so/) tool

### Acknowledgements

- Many thanks to my mentor Aaron for his timely feedback, encouragement and recommendations over the course of this project's development