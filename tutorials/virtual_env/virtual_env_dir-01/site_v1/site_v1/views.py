# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from .models import Account, UserAccount

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    user = request.user
    if(not request.user.is_authenticated()):
        return HttpResponse("Homepage <a href='login'>Login</a>")
    else:
        return render(request, 'consumer_datapoint/index.html',{
            'username':request.user.username,
            'logo': 'logo',
            'page':index.__name__,
            'app_links':"consumer_datapoint",
            'login':"logout",
        })
        # return HttpResponse("You're looking at <b> %s's</b> homepage!   <a href='logout'>Logout</a>" % user.username)
