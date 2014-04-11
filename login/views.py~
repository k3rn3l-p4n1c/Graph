from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
import cgi
from vertex.models import Vertex
from time import sleep
from urllib import urlencode

def view(request):
	query = request.META['QUERY_STRING']
	msg = ""
	if query:
		msg = cgi.parse_qs(query)['server_message'][0]
	return render_to_response('firstpage.html',
		{"SERVER_MESSAGE":msg},
		context_instance=RequestContext(request))

def login(request):
	try:
		eml = request.POST['email']
		pwd = request.POST['password']
	except :
		return HttpResponse('Error')
	
	try:
		client = Vertex.objects.get(email = eml)
		if client.password != pwd:
			raise LookupError()
	except :
		sleep(3)
		d = {'server_message':"Wrong username or password."}
		query_str = urlencode(d)
		return HttpResponseRedirect('/login/?'+query_str)
	
	response = HttpResponseRedirect('/home/')
  	response.set_cookie( 'email' , eml )
  	response.set_cookie( 'password' , pwd)
  	return response

def logout(request):
	response = HttpResponseRedirect('/')
	response.delete_cookie('email')
	response.delete_cookie('password')
	return response
    
# Create your views here.
