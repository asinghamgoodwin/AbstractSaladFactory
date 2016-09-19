from django.conf.urls import url

from . import views

app_name = 'salads'
urlpatterns = [
        url(r'^(?P<salad_id>[0-9]+)/saladStatus/$', views.saladStatus, name='saladStatus'),
        url(r'^(?P<salad_id>[0-9]+)/commitment/$', views.commitment, name='commitment'),
        url('createSalad', views.createSalad, name='createSalad'),
        url('saladCreated', views.saladCreated, name='saladCreated'),
        ]
