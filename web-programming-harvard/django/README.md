# Django

When we install Django, we get django-admin, which provides new command line options.

To start a new project, use `django-admin startproject projectname`. This creates a project with default files. It includes `manage.py` script which is used to manage the applications.

`django-admin startproject mysite` creates *mysite* folder with following files.

- `__init__.py` tells that this is a Python package.
- `settings.py` includes settings for this project.
- `urls.py` includes URL routing for top level as well all application level routes.
- `wsgi.py` is used for deploying the app to server

To create a new route, create a function in `views.py`. Provide routing for this function in `urls.py`. In project level, URL include urls file for this application.

When we create new application, we need to add the application into `settings.py` file in INSTALLED_APPS.

To start the application, run from project level directory `python manage.py runserver`. We can run development server on a custom host and port by loading a different setting file `python manage.py runserver 127.0.0.1:8001 --settings=mysite.settings`

The settings in `settings.py` include:
- DEBUG: This turns on debug mode. When moving to production, this must be set to False.
- ALLOWED_HOSTS: It is not applied when debug mode is on or when tests are run. In production mode, you will have to add your domain/host to this setting in order to allow it to serve your site.
- INSTALLED_APPS: It is a setting that will be edited for all projects. This setting tells Django which applications are active for this site. By default Django includes following apps.
    - `django.contrib.admin`: An administration site
    - `django.contrib.auth`: authentication framework
    - `django.contrib.contenttypes`: framework for handling content types
    - `django.contrib.sessions`: session framework
    - `django.contrib.messages`: messaging framework
    - `django.contrib.staticfiles`: framework for managing static files

- MIDDLEWARE: a list that contains middleware to be executed.
- ROOT_URLCONF: indicates Python modeul where the root URL patterns of your application are defined.
- DATABASES: a dictionary that contains the settings for all databases to be used in the project. There must be a default database.
- LANGUAGE_CODE: defines the default language code for this site
- USE_TZ: tells Django to activate/deactivate timezone support. This setting is set to True when you create a new project using `startproject` command.

In Django, an application is a group of models, views, templates and URLs. Applications interact with the framework to provide some specific functionalities and may be reused in various projects. When we create project using `python manage.py startproject <proj_name>`. It creates following files.

- `admin.py`: This is where we register models to include them in Django administration site-using the Django admin site is optional.
- `apps.py`: This includes main configuration for <proj_name> application.
- `migrations`: contain database migrations of your application.
- `models.py`: Data models of application - All applications need to have a model file, but it can be empty.
- `tests.py`: This is where you can write tests for application
- `views.py`: logic of application.

Django also allows for incrementally updating the schema (model) of different objects using migrations. Django includes ORM and we only need to define classes for our objects as shown in [models.py](airline/flights/models.py). Django includes built-in types that maps to datatypes in SQL database. Now, once we made the changes to class, we can use migrations and it will update the schema of the database. 

`python manage.py makemigrations` will create migration required to database. It creates new file inside `migrations` directory. To see what will happen if we run this migration, we can use `python manage.py sqlmigrate flights 0001`. To make actual migrations, run `python manage.py migrate`. The database is defined inside `settings.py` file.

If you want to create objects manually, we can easily do it through shell.
To retrieve objects in readable format, we have to define `__str__` function inside models file.

```shell
python mange.py shell
from flights.models import Flight
f = Flight(origin="New York", destination="London", duration=415)
f.save() # run commit on database
Flight.objects.all() # get all flights
f = Flight.objects.first() # get first flight
f.origin
f.destination
f.delete() # delete the flight from database
```

The templates are rendered from `templates` directory. If we want to add new objects, we can also use admin site. In order to do that, we need to register our classes into `admin.py` file. To access admin site, we need to login to admin site. For that, we need superuser.

`python manage.py createsuperuser`, Then go to `/admin` url where you'll use these login information.

When we define new models and we want to add model to administration site. We have to edit `admin.py` in our application. Django uses different form widgets for each type of field to display forms.

In Django, we can name different routes and then make urls based on this name in HTML. Check [flights app](airline/flights/views.py)

To add authentication, we can use built in authentication module. Check [example](authentication/users/views.py)

# Real Estate Django project

## FRONTEND PAGES

Home
About
Listings
Single Listing
Search
Register
Login
Dashboard (Inquiries)

## DESIGN SPECS
Use BTRE logo (Frontend and admin)
Branding colors – blue(#10284e) green(#30caa0)
Mobile Friendly
Social media icons & contact info
Doesn’t have to be too fancy but must be clean


## FUNCTIONALITY SPECS
Manage listings, realtors, contact inquiries and website users via admin
Role based users (staff and non-staff)
Display listings in app with pagination
Ability to set listings to unpublished
Search listings by keyword, city, state, bedrooms and price (Homepage & search page)
List realtors on about page with “seller of the month” (Control via admin)
Listing page should have fields listed below
Listing page should have 5 images with lightbox
Lightbox should scroll through images
Listing page should have a form to submit inquiry for that property listing
Form info should go to database and notify realtor(s) with an email
Frontend register/login to track inquiries
Both unregistered and registered users can submit form. If registered, can only submit one per listing



LISTING PAGE FIELDS

Title
Address, city, state, zip
Price
Bedrooms
Bathrooms
Square Feet
Lot Size
Garage
Listing Date
Realtor – Name & Image
Main image and 5 other images
# Use Virtual Environment

See dependencies installed globally using `pip3 freeze`.
To create virtual environment:

```shell
cd web-programming-harvard/django/
python3.7 --version # python3
python3.7 -m venv ./venv
# Activate the environment
source ./venv/bin/activate
# To deactivate
deactivate
# remove virtual environment
rmvirtualenv venv
# Activate the environment and run
python -V
pip install Django==2.1.1
pip freeze
```

Django comes with Django admin cli. You can see all the commands using `django-admin help`. Django creates `manage.py` with 

```shell
# create a new project named btre in present directory
django-admin startproject btre .
# start the server with
python manage.py runserver
# Create a new app
python manage.py startapp pages

pip install autopep8
python manage.py collectstatic # This copies static files and puts them in the base static directory
```


When we extend a template, that should be the first line on the child template page.
To install PostgreSQL on Ubuntu


```shell
sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib python3-dev 
sudo su - postgres
psql
postgres-# \conninfo
# Create password for 'postgres' user
\password
# Create database
CREATE DATABASE btredb OWNER postgres;
postgres-# \q
```

To run migrations,

```shell
python manage.py migrate
```

## Models

**Listings**

- id: INT
- realtor: INT (FOREIGN KEY to *realtor*)
- title: STR
- address: STR
- city: STR
- state: STR
- zipcode: STR
- description: TEXT
- price: INT
- bedrooms: INT
- bathrooms: DECIMAL
- garage: INT (zero as default)
- sqft: INT
- lot_size: FLOAT (area)
- is_published: BOOL (default to be true)
- list_date: DATE
- photo_main: STR
- photo_1: STR
- photo_2: STR
- photo_3: STR
- photo_4: STR
- photo_5: STR
- photo_6: STR

**Realtor**

- id: INT
- name: STR
- photo: STR
- description: TEXT
- email: STR
- phone: STR
- is_mvp: BOOL (default false)
- hire_date: DATE


**Contact** This is the inquiry sent by users

- id: INT
- user_id: INT
- listing: INT
- listing_id: INT
- name: STR
- email: STR
- phone: STR
- message: TEXT
- contact_date: DATE


After creating models, run make migrations to make migrations file.

```shell
pip install Pillow
python manage.py makemigrations
# or for specific model
# python manage.py makemigrations listings
python manage.py sqlmigrate listings 0001 # shows the listings sql command that will run with 0001 migration file
python manage.py migrate