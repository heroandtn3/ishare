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

    url(r'^img/json/recent_comment/(?P<photo_id>\d+)/$',
        views.photo_json_recent_comment, name='photo_json_recent_comment'),

    url(r'^img/json/send_comment/(?P<photo_id>\d+)/$',
        views.photo_json_send_comment, name='photo_json_send_comment'),

    url(r'^img/json/vote/(?P<photo_id>\d+)/$',
        views.photo_json_vote, name='photo_json_vote'),

    url(r'^album/(?P<album_id>\d+)/$',
        views.album_detail, name='album_detail'),
)