from django.conf.urls import patterns, url

from vertex import views

urlpatterns = patterns('',
    # ex: /vertex/5/
    url(r'^(?P<user_id>\w+)/$', views.profile, name='profile'),
)
