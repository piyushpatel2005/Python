# Bookmarks social website

```shell
django-admin startproject bookmarks
cd bookmarks/
django-admin startapp account
```

After adding new app to INSTALLED_APPS in `settings.py` file. Run `python manage.py migrate`.

Django comes with built-in authentication framework that can handle user authentication, sessions, permissions and user groups.This includes views for common user actions like login, logout, password change and password reset. It is located at `django.contrib.auth`. It contists of auth application and the two middlewares; `AuthenticationMiddleware` - associates user with requests using sessions and `SessionMiddleware` - handles the current session across requests. The authentication framework. The authentication framework also includes following models:
- `User` including username, password, email, first_name, last_name and is_active fields
- `Group` to categorize users
- `Permission` flag for users or groups to perform actions.