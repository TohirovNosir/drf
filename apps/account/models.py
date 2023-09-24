from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None, **kwargs):
        if username is None:
            raise TypeError({"success": False, "detail": "User should have a username"})
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(username=username, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    username = models.CharField(max_length=221, unique=True, db_index=True)
    email = models.EmailField(max_length=221, unique=True, null=True, blank=True, db_index=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = AccountManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        name_list = []
        if self.last_name:
            name_list.append(self.last_name)
        if self.first_name:
            name_list.append(self.first_name)
        if name_list:
            return " ".join(name_list)
        return "-"
