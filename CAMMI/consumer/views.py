# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
# from django.template import loader
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login
from django.views.generic import View
# from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def consumerHome(request, account_id):
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'page': 'consumer app homepage',
            'message':"consumerHome"
        })

@login_required(login_url='/login/')
def listConsumers(request, account_id):
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'message':"consumerList"
        })

@login_required(login_url='/login/')
def listConsumer(request, account_id, consumer_id):
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'message':"consumerList"
        })

@login_required(login_url='/login/')
def modifyConsumer(request, account_id, consumer_id):
        return render(request, 'consumer/index.html',{
            # 'user':user,
            'message':"consumerList"
        })

@login_required(login_url='/login/')
def createConsumer(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def deleteConsumer(request, account_id, consumer_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def profileHome(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def viewProfile(request, account_id, profile_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def createProfile(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def modifyProfile(request, account_id, profile_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def deleteProfile(request, account_id, profile_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def dataPointHome(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def viewDataPoint(request, account_id, datapoint_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def createDataPoint(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def modifyDataPoint(request, account_id, datapoint_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def deleteDataPoint(request, account_id, datapoint_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def dataPointSetHome(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def viewDataPointSet(request, account_id, datapoint_set_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def createDataPointSet(request, account_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def modifyDataPointSet(request, account_id, datapoint_set_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })

@login_required(login_url='/login/')
def deleteDataPointSet(request, account_id, datapoint_set_id):
    return render(request, 'consumer/index.html',{
        # 'user':user,
        'message':"consumerCreate "
    })
