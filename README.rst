django-cookbook
===============

Recipes for Django apps

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: MIT

Initial Setup
-------------

To setup the app you'll need to have [docker installed and run the following](http://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html)::

   $ docker-compose -f local.yml build
   $ docker-compose -f local.yml up


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
.....................

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ ./djrun.sh python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
.............

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ ./djrun.sh coverage run -m pytest
    $ ./djrun.sh coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   $ ./djrun.sh pytest

Live reloading and Sass CSS compilation
.......................................

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html


Local Development
-----------------

Updating python requirements
............................

When updating python requirements (e.g. in `requirements/base.txt`), you'll need to rebuild the
docker container::

   $ docker-compose -f local.yml build
   $ docker-compose -f local.yml up


Deployment
----------

The following details how to deploy this application.


Docker
......

See detailed `cookiecutter-django Docker documentation`_.

{}
