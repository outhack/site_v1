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
def userHasAccess(request, account_id):
    if str(request.user.id) == account_id:
        return True
    else:
        return False

def pageNotFound(request):
    return render(request, 'security/page_not_found.html',{
        # 'user':user,
        # 'username':request.user.username,
        # 'page': 'consumer app homepage',
        # 'message':"consumerHome",
        'title':"Lo Siento!!!",
    })

@login_required(login_url='/login/')
def consumerHome(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/consumer_home.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Consumer Homepage",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def listConsumers(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_modify_delete.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Consumer List",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def listConsumer(request, account_id, consumer_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/view_consumer.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Consumer Details "+consumer_id,
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def modifyConsumer(request, account_id, consumer_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/modify_consumer.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Modify Consumer",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def createConsumer(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_consumer.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Create Consumer",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def deleteConsumer(request, account_id, consumer_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/delete_consumer.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Delete Consumer",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def profileHome(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_modify_delete.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Profile Home",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def viewProfile(request, account_id, profile_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/view_profile.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"View Profile",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def createProfile(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_profile.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Create Profile",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def modifyProfile(request, account_id, profile_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/modify_profile.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Modify Profile",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def deleteProfile(request, account_id, profile_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/delete_profile.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Delete Profile",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def dataPointHome(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_modify_delete.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"DataPoint Homepage",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def viewDataPoint(request, account_id, datapoint_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/view_datapoint.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"View DataPoint",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def createDataPoint(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_datapoint.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Clear DataPoint",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def modifyDataPoint(request, account_id, datapoint_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/modify_datapoint.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Modify DataPoint",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def deleteDataPoint(request, account_id, datapoint_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/delete_datapoint.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Delete DataPoint",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def dataPointSetHome(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_modify_delete.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"DataPoint Set Home",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def viewDataPointSet(request, account_id, datapoint_set_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/view_datapoint_set.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"View DataPoint Set",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def createDataPointSet(request, account_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/create_datapoint_set.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Create DataPoint Set",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def modifyDataPointSet(request, account_id, datapoint_set_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/modify_datapoint_set.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Modify DataPoint Set",
        })
    else:
        return pageNotFound(request)

@login_required(login_url='/login/')
def deleteDataPointSet(request, account_id, datapoint_set_id):
    if userHasAccess(request, account_id):
        return render(request, 'consumer/delete_datapoint_set.html',{
            'username':request.user.username,
            'page': 'consumer app homepage',
            'message':"consumerHome",
            'title':"Delete DataPoint Set",
        })
    else:
        return pageNotFound(request)
