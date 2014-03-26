from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from urllib import urlencode
from time import sleep
from vertex.models import Vertex

def home(request):
	print request.COOKIES
	try:
		eml = request.COOKIES[ 'email' ]
		pwd = request.COOKIES[ 'password' ]
	except KeyError:
		d = {'server_message':"You are not logged in."}
		query_str = urlencode(d)
		return HttpResponseRedirect('/login/?'+query_str)
	try:
		client = Vertex.objects.get(email = eml)
		if client.password != pwd:
			raise LookupError()
	except LookupError:
		sleep(3)
		d = {'server_message':"Wrong username or password."}
		query_str = urlencode(d)
		return HttpResponseRedirect('/login/?'+query_str)
	return render_to_response('home.html',
		{"USER_EMAIL":eml},
		context_instance=RequestContext(request))

# Create your views here.
