__author__ = 'Beryl'
from django.conf.urls import patterns, url
from note_app import views

urlpatterns = patterns('',
                       url(r'^add_note/$', views.add_note, name='add_note'),
                       url(r'$', views.index, name='index'),
                       )