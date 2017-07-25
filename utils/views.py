from django.shortcuts import render
from braces.views import GroupRequiredMixin, AnonymousRequiredMixin

class AdministratorOnlyMixin(GroupRequiredMixin):
    group_required = ["Administrator"]
    login_url = '/login/'

class ArtistsMixin(GroupRequiredMixin):
    group_required = ["Administrator","Artists"]
    login_url = '/login/'

class UsersMixin(GroupRequiredMixin):
    group_required = ["Users", "Administrator", "Artists"]
    login_url = '/login/'


# Create your views here.
