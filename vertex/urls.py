from django.conf.urls import patterns, url

from vertex import views

urlpatterns = patterns('',
    # ex: /vertex/bardia/
    url(r'^(?P<user_id>\w+)/$', views.profile, name='profile'),
)
