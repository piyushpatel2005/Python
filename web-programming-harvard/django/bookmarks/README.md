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

Create superuser `python manage.py createsuperuser`

Django provides following class-based views to deal with authentication located in `django.contrib.auth.views`.

- `LoginView`: handles a login form and logs in a user
- `LogoutView`: logs out a user
- `PasswordChangeView`: handles a form to change the user password
- `PasswordChangeDoneView`: The success view the user is redirected to after a successful password change.
- `PasswordResetView`: allows user to reset their password. It generates one time use link with a token and sends it to the user's email account.
- `PasswordResetDoneView`: tells user that an email - including a link to reset their password has been sent to them.
- `PasswordResetConfirmView`: allows users to set a new password
- `PasswordResetCompleteView`: The success view the user is redirected to after successfully resetting the password.

Put our `account` app at the top of INSTALLED_APPS so that Django uses our defined templates and not the default ones. By default Django looks at `templates/registration` directory for authentication views.
We create a `login.html` template inside `registration` directory. This includes `next` as hidden HTML input. This variable is first set by login view and when we pass next parameter like `http://localhost:8000/account/login/?next=/account/`, Django login view will redirect the user to the given URL after a successful login.

To protect a specific view from being accessible to non-registered users, we can use `login_required` decorator as shown in [Dashboard view](bookmarks/account/../../account/views.py). If the user is not authenticated, it redirects the user to login URL with the originally requested URL as a GET parameter named `next`. Add few variables inside `settings.py` like,

- LOGIN_REDIRECT_URL: which URL to redirect after a successful login if no `next` parameter is present in request.
- LOGIN_URL: The URL to redirect the user to login
- LOGOUT_URL: URL to redirect the user to logout.

To display appropriate link depending on either user is logged in or not, HttpRequest object includes current user object. That can be accessed using `request.user`. A non-authenticated user is set in the request as an instance of `AnonymousUser`. We can check whether user is authenticated by accessing its read-only attribute `is_authenticated`.


## Password change

