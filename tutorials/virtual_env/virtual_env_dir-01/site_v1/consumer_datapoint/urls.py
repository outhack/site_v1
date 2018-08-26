from django.conf.urls import url

from . import views

app_name = 'consumer_datapoint'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^(?P<account_name>[\w\-]+)/(?P<pk>[0-9]+)$', views.UserAccountLandingView.as_view(), name='user_account'),
    url(r'^datapoints$', views.DataPointsView.as_view(), name='datapoints'),
    url(r'^datapoint/(?P<pk>[0-9]+)$', views.DataPointView.as_view(), name='datapoint'),
    url(r'^datapoint/create$', views.CreateDataPointView.as_view(), name='create_datapoint'),
    url(r'^datapoint_groups$', views.DataPointGroupsView.as_view(), name='datapoint_groups'),
    url(r'^datapoint_group/(?P<pk>[0-9]+)$', views.DataPointGroupView.as_view(), name='datapoint_group'),
    url(r'^datapoint_group/create$', views.CreateDataPointGroupView.as_view(), name='create_datapoint_group'),
    url(r'^profiles$', views.ProfilesView.as_view(), name='profiles'), #AKA consumer_datapoint
    url(r'^profile/(?P<pk>[0-9]+)$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/create$', views.CreateDataPointGroupView.as_view(), name='create_profile'),

    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
