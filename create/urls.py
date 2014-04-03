from django.conf.urls import patterns, url

from create import views

urlpatterns = patterns('',
	# http://127.0.0.1:8000/create/
	#http://127.0.0.1:8000/create/?firstname=bardia&lastname=heydari&email=az.bardia13%#40gmail.com&password=123123&year=1994&month=12&day=9&tel=09123456789&country=iran&city=tehran&sex=male&submit=Create
	url(r'^$', views.create, name='create'),
)
