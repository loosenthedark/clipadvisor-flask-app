<h1 align='center'>Clipadvisor Web Application</h1>



<p align="center"><img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" alt="Code Institute logo" width="200" height="auto"></p>
<p align="center"><img src="docs/images/screenshots/clipadvisor-logo.png" alt="Clipadvisor logo" width="200" height="auto"></p>



<p align="center" style="font-style:italic;">Code Institute Diploma in Software Development: Python and Data-Centric Development - Milestone Project</p>



<p align="center"><a href="https://clipadvisor-flask-app.herokuapp.com/" style="font-weight:bold;">Live link to deployed project</a> (hosted on GitHub Pages)</p>



---



**Clipadvisor** is a full-stack web application that boasts comprehensive CRUD functionality, allowing users to post, view, edit and delete reviews of barbers. Backend data processing is facilitated by Python+Flask in tandem with SQLAlchemy (via the Flask-SQLAlchemy extension). Dynamic templating logic has been put in place to enable visitors to navigate with ease and choose from an appropriate selection of frontend pages (routes), depending on whether they are logged in or out. The site offers a highly rewarding User Experience through the use of carefully-targetted colour schemes, fully-responsive design flourishes and smart interactivity. Overall, it comfortably fulfills its goal of being "a cut above" its competitors!



<p align="center"><img src="docs/images/screenshots/clipadvisor-landing.png" alt="Clipadvisor landing (Home) page screenshots across multiple device sizes" width="70%" height="auto"></p>



## User Experience (UX)

As we emerge from Level-5 lockdown, and normality slowly returns to the services and retail sectors, the majority of us will be looking forward to getting a long-overdue and much-needed haircut. Given that this set of circumstances will likely result in long waiting lists at barbers everywhere, it would be nice to know which businesses are worth waiting for and which should best be avoided.

That's where Clipadvisor comes in, offering users a convenient, trustworthy and authoritative source of barbershop ratings and reviews.

As with any such application, the best way to showcase Clipadvisor's benefits and features is to profile a number of **User Stories** pertaining to typical visitors to the site. With this in mind, a list of such User Stories might include (but by no means be limited to) the following:

1. "As a first-time user, I would like to be able to CREATE a review of a barber I visited recently."
2. "As a first-time user, I would like to be able to READ reviews of barbers posted previously by others."
3. "As a returning user, I would like to be able to UPDATE a review I posted recently."
4. "As a returning user, I would like to be able to DELETE a review I posted recently."
5. "As a Clipadvisor user, I would like to be able to contact the site owner(s) with a specific query."
6. "As a developer and frequent site user, I would like to be able to contact the site owner(s) to offer feedback on the app's functionality."
7. "As site owner, I would like to be able to moderate all user-submitted content, i.e. have the ability to UPDATE and/or DELETE reviews where necessary."
8. "As site owner, I would like for users to be able to contact me directly, i.e. without having to leave the application."



On the **Design** front, a [Material Design for Bootstrap](https://mdbootstrap.com/) stylesheet was used to give the site its overall look and feel - more specifically, the [MDB jQuery 3 (default Bootstrap 4 version)](https://mdbootstrap.com/docs/b4/jquery/) was chosen for this purpose.



The traditional 'barbers pole' **colours** of red, blue and white are employed throughout. The particular shades of red and blue (given the class names `.barber-red` and `.barber-blue`, respectively, in the site's custom stylesheet) are taken from [this Shutterstock 'barber shop icon'](https://www.shutterstock.com/image-vector/barber-symbol-shop-icon-hair-service-1070505362?id=1070505362&irclickid=1jiSOcU5OxyLUmQwUx0Mo3EqUkEXh30ItXjY1M0&irgwc=1&utm_medium=Affiliate&utm_campaign=Free%20SVG&utm_source=2022575&utm_term=&c3ch=Affiliate&c3nid=IR-2022575), and lend visual clarity and consistency to the site.



In terms of **font** preferences, things were kept pretty simple: Roboto was chosen for the vast majority of site text; this is complemented by [Roboto Condensed](https://fonts.google.com/specimen/Roboto+Condensed?query=roboto+conde) for most headings as well as the Clipadvisor logo `.navbar-brand` element.



From the perspective of **imagery**, the site's background hero image (a hand-drawn sketch featuring a variety of barbershop utensils) is a stock illustration [taken from Shutterstock's library](https://www.shutterstock.com/image-illustration/barber-shop-seamless-pattern-hand-drawn-1715625478). The aforementioned ['barbers pole' icon](https://www.shutterstock.com/image-vector/barber-symbol-shop-icon-hair-service-1070505362?id=1070505362&irclickid=1jiSOcU5OxyLUmQwUx0Mo3EqUkEXh30ItXjY1M0&irgwc=1&utm_medium=Affiliate&utm_campaign=Free%20SVG&utm_source=2022575&utm_term=&c3ch=Affiliate&c3nid=IR-2022575), used for the site's favicon as well as to accompany most of the main headings, is also used with permission from Shutterstock. All other icons are imported from [Font Awesome](https://fontawesome.com/).



All pre-existing site content (user profiles, barbershop names, reviews etc.) at the time of writing is purely generic filler text compiled by the site's creator for the sake of authenticity.



---



* [Flask + SQLAlchemy CRUD application tutorial | Parwiz Forogh on YouTube](https://www.youtube.com/watch?v=XTpLbBJTOM4)

* [Python website with database connectivity and user authentication tutorial | Tech With Tim on YouTube ](https://www.youtube.com/watch?v=dam0GPOAvVI)

* Auto-generated 'secret key' password supplied by [this key-gen tool](https://passwordsgenerator.net/)

* https://www.shutterstock.com/image-vector/barber-symbol-shop-icon-hair-service-1070505362?id=1070505362&irclickid=1jiSOcU5OxyLUmQwUx0Mo3EqUkEXh30ItXjY1M0&irgwc=1&utm_medium=Affiliate&utm_campaign=Free%20SVG&utm_source=2022575&utm_term=&c3ch=Affiliate&c3nid=IR-2022575

* A way of disabling 'false positive' error messages thrown by [Pylint](https://pypi.org/project/pylint/) in relation to the `scoped_session` class ("instance of scoped_session has no add/commit member" etc.) [found here](https://stackoverflow.com/questions/59214324/flask-error-db-scoped-session-instance-of-scoped-session-has-no-commit-mem)

* Bespoke 'page rating' code snippet used within `#review-submit-form` adapted from [this template](https://codepen.io/hesguru/pen/BaybqXv)

* `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres` [fix](sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres)

* Flask-SQLAlchemy Pagination tutorial: https://www.youtube.com/watch?v=PSWf2TjTGNY

* I was able to make flash messages more visually appealing by adding some basic markup (for line breaks etc.) using the [`flask.Markup` extension](https://tedboy.github.io/flask/generated/generated/flask.Markup.html) after following advice posted on [this Stack Overflow thread](https://stackoverflow.com/questions/18225713/how-to-display-html-content-through-flask-messages)

* Material Design 'block' components for Reviews page adapted from [Marta Wierzbicka's original design](https://mdbootstrap.com/snippets/jquery/marta-szymanska/1343674)

* [jQuery DateTimePicker plugin source code](https://github.com/xdan/datetimepicker)

* Users are required to supply at least one available payment method when submitting a review by means of a [jQuery validation script that has been with permission](https://www.howtocodeschool.com/2019/11/submit-form-If-at-least-one-checkbox-is-checked.html)

* After trying everything (including chatting with Igor on the Code Institute Tutor Assistance tab) right up to starting a brand new environment, and then uninstalling and reinstalling all of the package dependencies from my `requirements.txt` file (none of which resolved the issue), I finally figured out that the cause of a persistent `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres` error was a bug linked to how SQLAlchemy stores the dialect for the project's Database URI (environment variable). After following the advice [on this forum](https://github.com/pallets/flask-sqlalchemy/issues/929), I was eventually able to overcome this problem by modifying the DB URI dialect in my `app.py` file

* Dynamic-width Flash message alert implemented with help from [this Stack Overflow response](https://stackoverflow.com/questions/31721816/set-divs-width-equal-to-another-div); augmented by [alert resize on screen resize](https://api.jquery.com/resize/)

* Font Awesome SVG attribution [ link to licence](https://fontawesome.com/license)

* I got some help with using the appropriate Jinja syntax when trying to display reviews in descending order of recency (i.e. sorting the list returned from my database by id in reverse order) from [this Stack Overflow thread](https://stackoverflow.com/questions/1959386/how-do-you-sort-a-list-in-jinja2)

* I received pointers for generating email from contact form user input in Python from [this video tutorial](https://www.youtube.com/watch?v=JRCJ6RtE3xU)

* Customer error handling has been put in place to deal with three of the most common error codes [in keeping with best practices](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/)

* https://stackoverflow.com/questions/17797921/jinja2-create-new-row-for-every-3-items | https://jinja.palletsprojects.com/en/2.11.x/templates/#batch