from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
import cgi
from vertex.models import Vertex
from time import sleep
from urllib import urlencode
from django.contrib.auth import authenticate, login


def view(request):
	query = request.META['QUERY_STRING']
	msg = ""
	print authDetail(request)
	if authDetail(request)[0] == True:
		print "redirect to home."
		return HttpResponseRedirect("/home/")
	if query:
		msg = cgi.parse_qs(query)['server_message'][0]
	return render_to_response('login.html',
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
	request.session['email'] = eml
	request.session['password'] = pwd
  	return response


def logout(request):
	response = HttpResponseRedirect('/')
	try:
		del request.session['email']
		del request.session['password']
	except:
		pass
	return response

def authDetail(request):
	try:
		eml = request.session[ 'email' ]
		pwd = request.session[ 'password' ]
	except:
		return [False,"..."]
	try:
		client = Vertex.objects.get(email = eml)
		if client.password != pwd:
			raise LookupError()
		print client
	except Vertex.DoesNotExist:
		return [False,"WRONG_USR"]
	except LookupError:
		return [False,"WRONG_PWD"]
	return [True,client]
    
# Create your views here.
