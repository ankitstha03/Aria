"""
A model for URL Mixin, timestamp

"""
# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import urllib.parse
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now as timezone_now
from django.conf import settings
from django.db.models import QuerySet

class UrlMixin(models.Model):
    """
    A replacement for get_absolute_url()
    Models extending this mixn should have
    either get_url or get_url_path implemented
    """
    class Meta:
        """
        Abstraction
        """
        abstract = True

    def get_url(self):
        if hasattr(self.get_url_path, "dont_recurse"):
            raise NotImplementedError
        try:
            path = self.get_url_path()
        except NotImplementedError:
            raise
        website_url = getattr(settings, "DEFAULT_WEBSITE_URL", "http://127.0.0.1:8000")
        return website_url + path
    get_url.dont_recurse = True

    def get_url_path(self):
        if hasattr(self.get_url, "dont_recurse"):
            raise NotImplementedError
        try:
            url = self.get_url()
        except NotImplementedError:
            raise
        bits = urlparse.urlparse(url)
        return urlparse.urlunparse(("","") + bits[2:])
    get_url_path.dont_recurse = True

    def get_absolute_url(self):
        return self.get_url_path()

class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def all_with_deleted(self):
        return super(SoftDeletionManager, self).get_queryset()

class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone_now())

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)

class CreationModificationDateMixin(models.Model):
    """
    Abstract base class with creation and modification date and
    time
    """
    created = models.DateTimeField(_("Creation date and time"), editable = False)

    modified = models.DateTimeField(_("modification date and time"), null=True, editable=False)
    deleted_at = models.DateTimeField(_("deteled date"), null=True, blank=True, editable=False)
    objects = SoftDeletionManager()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone_now()
        else:
            if not self.created:
                self.created = timezone_now()
            self.modified = timezone_now()

            super(CreationModificationDateMixin, self).save(*args, **kwargs)
    save.alters_data = True

    def delete(self):
        self.deleted_at = timezone_now()
        self.save()
    def hard_delete(self):
        super(CreationModificationDateMixin, self).delete()

    class Meta:
        abstract = True


