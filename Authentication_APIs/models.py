from django.db import models

# Create your models here.
# auth_api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'   # use email for login
    REQUIRED_FIELDS = ['username']  # username still required

    def __str__(self):
        return self.email
