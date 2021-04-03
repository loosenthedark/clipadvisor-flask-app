![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

* [Flask + SQLAlchemy CRUD application tutorial | Parwiz Forogh on YouTube](https://www.youtube.com/watch?v=XTpLbBJTOM4)

* [Python website with database connectivity and user authentication tutorial | Tech With Tim on YouTube ](https://www.youtube.com/watch?v=dam0GPOAvVI)

* Auto-generated 'secret key' password supplied by [this key-gen tool](https://passwordsgenerator.net/)

* https://www.shutterstock.com/image-vector/barber-symbol-shop-icon-hair-service-1070505362?id=1070505362&irclickid=1jiSOcU5OxyLUmQwUx0Mo3EqUkEXh30ItXjY1M0&irgwc=1&utm_medium=Affiliate&utm_campaign=Free%20SVG&utm_source=2022575&utm_term=&c3ch=Affiliate&c3nid=IR-2022575

* A way of disabling 'false positive' error messages thrown by [Pylint](https://pypi.org/project/pylint/) in relation to the `scoped_session` class ("instance of scoped_session has no add/commit member" etc.) [found here](https://stackoverflow.com/questions/59214324/flask-error-db-scoped-session-instance-of-scoped-session-has-no-commit-mem)

* Bespoke 'page rating' code snippet used within `#review-submit-form` adapted from [this template](https://codepen.io/hesguru/pen/BaybqXv)

* `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres` [fix](sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres)

* I was able to make flash messages more visually appealing by adding some basic markup (for line breaks etc.) using the [`flask.Markup` extension](https://tedboy.github.io/flask/generated/generated/flask.Markup.html) after following advice posted on [this Stack Overflow thread](https://stackoverflow.com/questions/18225713/how-to-display-html-content-through-flask-messages)

* Material Design 'block' components for Reviews page adapted from [Marta Wierzbicka's original design](https://mdbootstrap.com/snippets/jquery/marta-szymanska/1343674)

* [jQuery DateTimePicker plugin source code](https://github.com/xdan/datetimepicker)

* Users are required to supply at least one available payment method when submitting a review by means of a [jQuery validation script that has been with permission](https://www.howtocodeschool.com/2019/11/submit-form-If-at-least-one-checkbox-is-checked.html)

* After trying everything (including chatting with Igor on the Code Institute Tutor Assistance tab) right up to starting a brand new environment, and then uninstalling and reinstalling all of the package dependencies from my `requirements.txt` file (none of which resolved the issue), I finally figured out that the cause of a persistent `sqlalchemy.exc.NoSuchModuleError: Can't load plugin: sqlalchemy.dialects:postgres` error was a bug linked to how SQLAlchemy stores the dialect for the project's Database URI (environment variable). After following the advice [on this forum](https://github.com/pallets/flask-sqlalchemy/issues/929), I was eventually able to overcome this problem by modifying the DB URI dialect in my `app.py` file

* Font Awesome SVG attribution [ link to licence](https://fontawesome.com/license)