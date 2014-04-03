from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect

def firstpage(request):
	try:
		eml = request.COOKIES['email']
		pwd = request.COOKIES['password']
	except :
		return HttpResponseRedirect('/home/')
	print 'Graph/Graph/views.py: usr:',eml,'  pwd: ',pwd
	return HttpResponseRedirect('/home/')

# Create your views here.
