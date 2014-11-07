from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'ishare.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ishare/', include('ishare.urls', namespace='ishare')),
    url(r'^account/', include('account.urls', namespace='account')),
)
