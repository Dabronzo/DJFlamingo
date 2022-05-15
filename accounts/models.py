from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomAccountManager(BaseUserManager):
    """The manager class to the custom user creation class"""

    def create_superuser(self, email, user_name, password, **others):
        """Function to create the superuser"""

        others.setdefault('is_superuser', True)
        others.setdefault('is_staff', True)

        if others.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        
        if others.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.'
            )

        return self.create_user(email, user_name, password, **others)

    def create_user(self, email, user_name, password, **others):
        """Function base user creation that returns a user"""

        if not email:
            raise ValueError(_('You must provide a email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **others)
        user.set_password(password)
        user.save()

        return user


class NewDjUser(AbstractBaseUser, PermissionsMixin):
    """Custom user class to be used on the application"""

    email = models.EmailField(_("email address"), unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    join_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def __str__(self):
        """string method"""
        return f"{self.user_name}"


