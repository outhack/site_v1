# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse
# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from .models import Account, UserAccount

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout


def index(request):
    user = request.user
    if(not request.user.is_authenticated()):
        # return HttpResponse("Homepage <a href='login'>Login</a>")
        return render(request, 'consumer_datapoint/index.html',{
            'page':"Welcome",
            'login':"login",
        })
    else:
        return render(request, 'consumer_datapoint/index.html',{
            'username':request.user.username,
            'logo': 'logo',
            'page':"Home",
            'app_links':"consumer_datapoint",
            'login':"logout",
        })
        # return HttpResponse("You're looking at <b> %s's</b> homepage!   <a href='logout'>Logout</a>" % user.username)

def login_user(request):
    # logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'consumer_datapoint/login.html', {
        'page': "Login",
        'logo': 'M-PSYCH'
    })

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
