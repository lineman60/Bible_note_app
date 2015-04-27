__author__ = 'Beryl'
from django.conf.urls import patterns, url
from note_app import views

urlpatterns = patterns('',
                       url(r'^add_note/$', views.add_note, name='add_note'),
                       url(r'^edit/(?P<id>\d+)/$', views.edit_note, name='edit_note'),
                      # url(r'^today/$', views.todays_readings, name='todays_readings'),
                        #TODO add lookup via /book/chap/vers in url
                        #TODO add view for todays readings
                       url(r'$', views.index, name='index'),

                       )