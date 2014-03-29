from django.conf.urls import patterns, url

from vertex import views

urlpatterns = patterns('',
    # ex: /vertex/bardia/    #ex: /vertex/bardia/like
    url(r'^(?P<user_id>\w+)/$', views.profile, name='profile'),
    url(r'^(?p<liker_id>\w+)/like/$',views.like_flow,name='like'),  

)
