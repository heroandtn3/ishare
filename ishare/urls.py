from django.conf.urls import patterns, url

from ishare import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^albums/$', views.albums, name='albums'),
)