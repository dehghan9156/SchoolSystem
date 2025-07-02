from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        extra_fields.setdefault("name", "Admin")
        extra_fields.setdefault("family", "User")
        extra_fields.setdefault("role", "admin")
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    Roel_User = [
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student'),
    ]
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    codemeli = models.CharField(max_length=10,blank=False,null=False)
    role = models.CharField(max_length=10, choices=Roel_User,blank=False,null=False)
    confirmation = models.BooleanField(default=False)  
    biography = models.TextField(blank=True, null=True) 
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()
