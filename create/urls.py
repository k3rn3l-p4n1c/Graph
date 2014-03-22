from django.conf.urls import patterns, url

from create import views

urlpatterns = patterns('',
    url(r'^/', views.create, name='create')
)
