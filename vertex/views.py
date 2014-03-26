from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from vertex.models import Vertex
   
def profile(request, user_id):
	try:
		vertex = Vertex.objects.get(user_id=user_id)
	except :
		return render_to_response('404error.html',
			{},
			context_instance=RequestContext(request))
	client = None
	try:
		eml = request.COOKIES[ 'email' ]
		pwd = request.COOKIES[ 'password' ]
		client = Vertex.objects.get(email = eml)
		if client.password != pwd:
			raise LookupError()
	except:
		client = None
	
	me = False
	if client:
		if client.user_id == vertex.user_id:
			me = True
	if me:
		return render_to_response('vertex.html',
			{"VERTEX_DETAIL":"yourself"},
			context_instance=RequestContext(request))
	else:
		return render_to_response('vertex.html',
			{"VERTEX_DETAIL":vertex.firstname+' '+vertex.lastname},
			context_instance=RequestContext(request))
	
	return HttpResponse("You're looking at vertex %s." % vertex)

# Create your views here.
