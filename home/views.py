from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def home(request):
	print request.COOKIES
	eml = request.COOKIES[ 'email' ]
	pwd = request.COOKIES[ 'password' ]
	#return HttpResponseRedirect('/login/')
	return HttpResponse("home "+eml)
# Create your views here.
