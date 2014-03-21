from django.conf.urls import patterns, url

from create import views

urlpatterns = patterns('',
    url(r'^create/', views.create, name='create')
)
