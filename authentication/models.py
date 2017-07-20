"""
File: models.py
Author: Shailesh Mishra
Github: https://github.com/rezera
Description:A model for user profile and its creation.
"""

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.models import CreationModificationDateMixin
from django.contrib.auth.models import User
import uuid
class UserProfiles(CreationModificationDateMixin):
    """
    User profile with extended  user model.
    The default user model is extended with addition of following fields.
    """
    ARTIST = 1
    USER = 2
    ROLE_CHOICE = (
            (ARTIST, 'Artist'),
            (USER, 'User'),
            )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("Username"), max_length=20, default='username')
    #user_role = models.IntegerField(max_length=1, null=True, choices=ROLE_CHOICE)
    bio = models.TextField(_("About"), max_length=500, default='')
    location = models.CharField(_("Location"), max_length=9, default='NEP')
