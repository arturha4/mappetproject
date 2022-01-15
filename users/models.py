from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_superuser(self, email, password, first_name, second_name, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_admin", True)
        other_fields.setdefault("is_superuser", True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                "is_staff must be True"
            )
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                "is_superuser must be True"
            )
        return self.create_user(email, password, first_name, second_name, **other_fields)

    def create_user(self, email, password, first_name, second_name, birthday, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, second_name=second_name, birthday=birthday,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user


class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    second_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=10, default=None)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'second_name', 'birthday']

    def __str__(self):
        return self.first_name + ' ' + self.second_name