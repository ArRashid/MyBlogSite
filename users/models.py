from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=100)
    pfp = models.ImageField(_('Profile Pic'),upload_to="uploads/users/profiles",blank=True,null=True)
    is_blog = models.BooleanField(default=False)
    is_team = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        permissions = (
            ('view_pizza', 'Can view pizza'),
        )
