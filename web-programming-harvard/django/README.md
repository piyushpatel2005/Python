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

To start the application, run from project level directory `python manage.py runserver`.

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

In Django, we can name different routes and then make urls based on this name in HTML. Check [flights app](airline/flights/views.py)

To add authentication, we can use built in authentication module. Check [example](authentication/users/views.py)