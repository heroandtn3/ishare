from django.conf.urls import patterns, url

from ishare import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
)