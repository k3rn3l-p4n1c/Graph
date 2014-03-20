from django.shortcuts import render
from django.http import HttpResponse
import os

def login(request):
	source_page = open("./template/login.html",'r').read()
	return HttpResponse(source_page)
    
# Create your views here.
