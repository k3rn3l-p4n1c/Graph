from django.shortcuts import render
from django.http import HttpResponse
import os

def create(request):
	source_page = open("./template/create.html",'r').read()
	return HttpResponse(source_page)
    
# Create your views here.
