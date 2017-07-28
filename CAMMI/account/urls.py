from django.conf.urls import url
from . import views

app_name = 'account'
urlpatterns = [
    #/account/
    url(r'^$', views.accountHome, name='account_home'),
    #ex: /account/users/
    # url(r'^users/$', views.listAccountUsers, name='list_users'),
    # #ex: /account/users/223/
    # url(r'^users/(?P<user_id>[0-9]+)/$', views.showUser, name='list_account_users'),
    # #ex: /account/users/create/
    # url(r'^users/create/$', views.createAccountUser, name='create_account_user'),
    # #ex: /account/users/modify/80/
    # url(r'^users/modify/(?P<user_id>[0-9]+)/$', views.listAccountUsers, name='list_account_users'),
    # #ex: /account/users/delete/324/
    # url(r'^users/delete/(?P<user_id>[0-9]+)/$', views.listAccountUsers, name='list_account_users'),

    #ex: /account/settings/
    # url(r'^settings/$', views.listAccountSettings, name='list_account_settings'),
]
