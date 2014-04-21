from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from urllib import urlencode
from time import sleep
from vertex.models import *
from django.core.exceptions import ObjectDoesNotExist
from login.views import authDetail

def home(request):

	if not authDetail(request)[0]:
		sleep(3)
		d = {'server_message':authDetail(request)[1]}
		query_str = urlencode(d)
		return HttpResponseRedirect('/login/?'+query_str)
	else:
		client = authDetail(request)[1]
	
	vertex = Vertex.objects.get(email = client.email)
	flows = vertex.flow_set.order_by('-last_forward_date')[:5]
		
	return render_to_response('home.html',
		{"USER_EMAIL":client.email,"login":True,'VERTEX_DETAIL':client,'flows':flows},
		context_instance=RequestContext(request))

# Create your views here.
