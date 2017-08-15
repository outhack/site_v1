from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.contrib.auth.views import login
from django.core.urlresolvers import resolve
from django.contrib.auth.decorators import login_required


# Create your views here.
# app_set = ['consumer']
account_id = None
def loginAttempt(request):
    if request.user.is_authenticated():
        account_id = request.user.id
        return redirect("/" + str(account_id)+"/")

def evaluateAccountAccessByID(request, id):
    account_id = request.user.id

def displaySiteHomePage(request):
    if request.user.is_authenticated():
        account_id = request.user.id
        return redirect("/" + str(account_id)+"/")
    else:
        return redirect("/login/")

# @login_required(login_url='/login/')
# def evaluateAccountID(request, account_id):
#     # Change request.user.id to request.user.account_id
#     if str(request.user.id) == account_id:
#         return HttpResponseRedirect(reverse('account:home', args=(request.user.id,)))
#         # return render(request, 'consumer/index.html',{
#         #     'username':request.user.username,
#         #     'message':"accountHome",
#         #     'valid_user':request.user.id,
#         #     # 'username': account_id,
#         #     'page':'Account \'' + str(request.user.id) +'\' Home'
#         # })
#     else:
#         return render(request, 'security/page_not_found.html', {
#             'page': request.path_info,
#             'id': request.user.id,
#             'type': type(request.user.id) is int,
#             'type': type(account_id) is int,
#         })
#
# @login_required(login_url='/login/')
# def evaluateApp(request, account_id, app):
#     # Change request.user.id to request.user.account_id
#     if str(request.user.id) == account_id:
#         if app in app_set:
#             return render(request, 'consumer/index.html',{
#                 'username':request.user.username,
#                 'message':"consumer app homepages",
#                 'valid_user':request.user.id,
#                 # 'username': account_id,
#                 'page':'Consumer App Home',
#             })
#         else:
#             return render(request, 'security/page_not_found.html', {
#                 'page': request.path_info,
#                 'type': type(request.user.id) is int,
#                 'type': type(account_id) is int,
#             })
#     else:
#         return render(request, 'security/page_not_found.html', {
#             'page': request.path_info,
#             'type': type(request.user.id) is int,
#             'type2': type(account_id) is int,
#         })
#
# def pageNotFound(request):
#         return render(request, 'security/page_not_found.html', {
#             'page': request.path_info,
#             'type': type(request.user.id) is int,
#             # 'type2': type(account_id) is int,
#         })

######################################
        # if app is None:
        #     return redirect("/"+str(account_id))
        # else:
        #
        #     return redirect("/"+str(account_id)+"/"+app)

# def loginForm(request):
#     current_url_path = request.path_info
#     if request.user.is_authenticated() and current_url_path == "/login/":
#         return HttpResponseRedirect(reverse('consumer:list'))
#     else:
#         # return login(request)
#         template_name = 'security/login.html'
#         return render(request, template_name,{
#             'message':"loginForm",
#             'current_url':current_url_path
#         })

# def custom_login(request):
#     current_url = resolve(request.path_info).url_name
#     if request.user.is_authenticated() and current_url == "login/":
#         return HttpResponseRedirect(reverse('consumer:list'))
#     else:
#         return login(request)

    # username = request.POST['username']
    # if request.user.is_authenticated():
    #     user_id = user.user_id;
    #     return HttpResponseRedirect(reverse('account:home'))
    # else:
    #     return login(request)
    # checkUserAuthenticated(request, username)
    # user = get_object_or_404(User, username = request.POST['username'])
    # user = authenticate(username=request.POST['username'], password=request.POST['password'])
    # if user is not None:
    #     login(request, user)
    #     return render(request, 'consumer/index.html', {
    # 			'username':request.POST['username'],
    #             'password':request.POST['password'],
    #             'status': request.user.is_authenticated(),
    #             'valid_user': "Yay!"
    #     })
    # else:
    #     return render(request, 'consumer/index.html', {
    # 			'username':request.POST['username'],
    #             'password':request.POST['password'],
    #             'status': request.user.is_authenticated(),
    #             'valid_user': "Nay!"
    #     })


#
# def checkUserAuthenticated(request, username):
#     user = User.objects.filter(username='username')
#     if request.user.is_authenticated():
#         return render(request,'security/login.html',{
#             'error_message' : "Logged In",
#         })
#     else:
#         template_name = 'security/login.html'
#         return render(request, template_name,{
#             'error_message':"loginForm"
#         })
