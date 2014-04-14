from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Graph import views
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Graph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.firstpage , name = 'firstpage'),
	url(r'^login/', include('login.urls')),
	url(r'^home/', include('home.urls')),
	url(r'^create/', include('create.urls')),
	url(r'^vertex/', include('vertex.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chat/', include('chat.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
urlpatterns += staticfiles_urlpatterns()
