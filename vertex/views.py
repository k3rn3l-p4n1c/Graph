from django.shortcuts import render
from django.http import HttpResponse
from vertex.models import Vertex
   
def profile(request, user_id):

	vertex = Vertex.objects.get(user_id=user_id)
	return HttpResponse("You're looking at vertex %s." % vertex)

# Create your views here.
