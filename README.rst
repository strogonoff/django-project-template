Django template for a web app with AngularJS on the client
==========================================================

Things included:

* A requirements.txt (warning: out-of-date Django there)
* Favicons and apple-touch-icons (hitched from h5bp)
* AngularJS client-side scaffolding
* Sphinx-based documentation scaffolding
* Static asset minification / concatenation with django-pipeline
* shell_plus, runserver_plus utility commands will be available

Roadmap:

* Update for latest Django
* Offer a way to quickly bootstrap the project inside a VM instead of
  virtualenv (Ansible playbook and Vagrantfile stubs, probably)
* Remove some of the default deps (captcha? Pillow?)

Initial setup
-------------

Install requirements that are not Python modules.

* PostgreSQL 9.1.9
* Python 2.7.0 and ``virtualenv`` / ``virtualenvwrapper``
* libjpeg, zlib, libfreetype
  are needed by ``pillow`` and ``django-simple-captcha``.
  Install using brew under OS X, apt-get under Ubuntu.
  https://pypi.python.org/pypi/Pillow/2.1.0

Create PostgreSQL database for the project.

Initialize virtual environment using ``virtualenv`` / ``virtualenvwrapper``.
Install Django 1.5 in there (``pip install django==1.5``).

Create a project using this template::

    $ django-admin.py startproject \
    --template=https://github.com/strogonoff/django-project-template/archive/master.zip \
    --extension=py --name=.gitignore \
    your_project_name

Initialize Git repository in ``your_project_name`` directory::

    $ cd your_project_name; git init

Put correct settings for this your development environment in settings.py
(such as DB access settings). settings.py should not be versioned, it contains
specific local settings and secrets.

Install requirements into virtual Python environment::

    $ pip install -r requirements.txt

Initialize the DB::

    $ ./manage.py syncdb
    Syncing...

    $ ./manage.py migrate
    Running migrations...

Run tests, development server, Django console to make sure installation works::

    $ ./manage.py test
    Ran 500 tests in 20s
    OK

    $ ./manage.py runserver_plus 0.0.0.0:8000
    Development server is running at http://0.0.0.0:8000/

    $ ./manage.py shell_plus
    Python 2.7.1
    >>>

Make sure that Site object has correct domain name/port set
(http://example.com/admin/sites/site/1/).

See DEVELOPMENT.txt for some further guidelines.

Building docs
-------------

Get Sphinx in your virtual environment::

    $ pip install sphinx

From ``docs/`` directory, build HTML documentation::

    $ make html

Then open ``build/html/index.html``.
