from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = 'Manager', 'Manager'
        EMPLOYEE = "EMPLOYEE", "Employee"

    username = models.CharField(_("Username"), max_length=50, unique=True)
    email = models.EmailField(_("Email"), max_length=100, unique=True)

    role = models.CharField(_("Role"), choices=Role.choices, blank=True, null=True)

    manager = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]


    def __str__(self):
        return self.username
