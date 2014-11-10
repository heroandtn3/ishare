from django.conf.urls import patterns, url

from ishare import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),

    url(r'^upload/$', views.upload, name='upload'),

    url(r'^albums/$', views.albums, name='albums'),

    url(r'^img/detail/(?P<photo_id>\d+)/$',
        views.photo_detail, name='photo_detail'),
    
    url(r'^img/direct/(?P<photo_id>\d+)/$',
        views.photo_direct, name='photo_direct'),
)