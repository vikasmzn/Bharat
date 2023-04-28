from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using = self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=500,unique = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
            return self.is_admin

    def has_module_perms(self, app_label):
            return self.is_admin