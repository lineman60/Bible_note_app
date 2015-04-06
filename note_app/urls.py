__author__ = 'Beryl'
from django.conf.urls import patterns, url
from note_app import views

urlpatterns = patterns('',
                       url(r'$', views.index, name='index')
                       )