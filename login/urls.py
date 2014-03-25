from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.view, name='view'),
    url(r'^login', views.login, name='login'),
    url(r'^logout', views.logout , name = 'logout'),
)
