from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

    def _str_(self):
        return self.username

