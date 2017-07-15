from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index1'))

