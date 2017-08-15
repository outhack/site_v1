from django.conf.urls import url
from . import views

app_name = 'security'
urlpatterns = [
    #/login/
    # url(r'^$', views.loginForm, name='login_form'),
    #/login/attempt
    url(r'^login_attempt/$', views.loginAttempt, name='login_attempt'),
    url(r'^$',views.displaySiteHomePage, name='display_site_homepage'),
    # url(r'^(?P<account_id>\d)/(?P<app>[a-z]+)/$|^(?P<account_ids>\d)/$|^(?P<account_idx>\d)$', views.evaluateURL, name='evaluate_url'),
    # url(r'^(?P<account_id>\d+)/$',views.evaluateAccountID, name='evaluate_account_id'),
    # url(r'^(?P<account_id>\d+)/(?P<app>[a-z]+)/$',views.evaluateApp, name='evaluate_app'),
    # url(r'^', views.pageNotFound, name='page_not_found'),


]
