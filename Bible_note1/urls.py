from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Bible_note1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^note/', include('note_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
