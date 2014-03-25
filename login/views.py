from django.shortcuts import render
from django.http import HttpResponse
import os

def login(request):
	#source_page = open("./template/index.html",'r').read()
	print 'VIEW',request.POST
	return HttpResponse("Login")
    
# Create your views here.
