from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.models import CreationModificationDateMixin
from django.contrib.auth.models import User

class UserProfiles(CreationModificationDateMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(_("Username"), max_length=20, default='username')
    bio = models.TextField(_("About"), max_length=500, default='')
    location = models.CharField(_("Location"), max_length=9, default='NEP')
