# Personal blog site

This project uses Django 2.0.5

Extra PostgreSQL is required using:

```shell
sudo apt-get install libpg-dev python-dev
sudo apt-get install postgresql postgresql-contrib
sudo su - postgres
create database blog; # create new password
create user blog with encrypted password 'blog';
# Give ownership of new `blog` database to `blog` user
grant all on database blog to blog;
```

When we create new database, we need to migrate again and create a separate super user using `python manage.py createsuperuser` for new database data.