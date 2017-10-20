from django.conf.urls import url
from . import views

app_name = 'consumer'
urlpatterns = [
    #/consumer/
    url(r'^$', views.consumerHome, name='consumer_home'),
	#ex: /consumer/list/
	url(r'^list/$', views.listConsumers, name='consumer_list'),
    #ex: /consumer/list/45/
	url(r'^list/(?P<consumer_id>[0-9]+)/$', views.listConsumer, name='view_consumer'),
    #ex: /consumer/list/create/
    url(r'^list/create/$', views.createConsumer, name='create_consumer'),
    #ex: /consumer/list/modify/45/
	url(r'^list/modify/(?P<consumer_id>[0-9]+)/$', views.modifyConsumer, name='modify_consumer'),
    #ex: /consumer/list/delete/45/
	url(r'^list/delete/(?P<consumer_id>[0-9]+)/$', views.deleteConsumer, name='delete_consumer'),

    #Profile
    #ex /consumer/profile/
    url(r'^profile/$', views.profileHome, name='profile_home'),
    #ex: /consumer/profile/2/
    url(r'^profile/(?P<profile_id>[0-9]+)/$', views.viewProfile, name='view_profile'),
    #ex: /consumer/profile/create/
    url(r'^profile/create/$', views.viewCreateProfile, name='view_create_profile'),

    url(r'^profile/create/(?P<ssn>[0-9]+)/$', views.createProfile, name='create_profile'),
    #ex: /consumer/profile/modify/66
    url(r'^profile/modify/(?P<profile_id>[0-9]+)/$', views.modifyProfile, name='modify_profile'),
    #ex: /consumer/profile/delete/66
    url(r'^profile/delete/(?P<profile_id>[0-9]+)/$', views.deleteProfile, name='delete_profile'),

    #DataPoint
    #ex: /consumer/datapoint/
    url(r'^datapoint/$', views.dataPointHome, name='datapoint_home'),
    #ex: /consumer/datapoint/55/
    url(r'^datapoint/(?P<datapoint_id>[0-9]+)/$', views.viewDataPoint, name='view_datapoint'),
    #ex: /consumer/datapoint/create/
    url(r'^datapoint/create/$', views.createDataPoint, name='create_datapoint'),
    #ex: /consumer/datapoint/modify/66/
    url(r'^datapoint/modify/(?P<datapoint_id>[0-9]+)/$', views.modifyDataPoint, name='modify_datapoint'),
    #ex: /consumer/datapoint/delete/32/
    url(r'^datapoint/delete/(?P<datapoint_id>[0-9]+)/$', views.deleteDataPoint, name='delete_datapoint'),


    #DataPointSet
    url(r'^datapoint_set/$', views.dataPointSetHome, name='datapoint_set_home'),
    #ex: /consumer/datapoint/55/
    url(r'^datapoint_set/(?P<datapoint_set_id>[0-9]+)/$', views.viewDataPointSet, name='view_datapoint_set'),
    #ex: /consumer/datapoint/create/
    url(r'^datapoint_set/create/$', views.createDataPointSet, name='create_datapoint_set'),
    #ex: /consumer/datapoint/modify/66/
    url(r'^datapoint_set/modify/(?P<datapoint_set_id>[0-9]+)/$', views.modifyDataPointSet, name='modify_datapoint_set'),
    #ex: /consumer/datapoint/delete/32/
    url(r'^datapoint_set/delete/(?P<datapoint_set_id>[0-9]+)/$', views.deleteDataPointSet, name='delete_datapoint_set'),
]
