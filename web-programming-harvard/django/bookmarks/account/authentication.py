from django.contrib.authe.models import User


class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """

    def authenticate(self, request, username=None, password=None):
        try:
            # get user by email address
            user = User.objects.get(email=username)
            # This method handles password hashing to compare given password against stored password
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
