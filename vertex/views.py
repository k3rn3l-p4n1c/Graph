from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from vertex.models import Vertex,Edge
   
def profile(request, user_id):
	client = None
	try:
		eml = request.COOKIES[ 'email' ]
		pwd = request.COOKIES[ 'password' ]
		client = Vertex.objects.get(email = eml)
		if client.password != pwd:
			raise LookupError()
	except:
		client = None
		
	try:
		vertex = Vertex.objects.get(user_id=user_id)
	except :
		return render_to_response('404error.html',
			{},
			context_instance=RequestContext(request))
		
	me = False
	if client:
		if client.user_id == vertex.user_id:
			me = True
	
	if request.POST and client and not me:
		try:
			new_edge = Edge.objects.get(vertex_tail_id = client.user_id,vertex_head_id = user_id)
		except:
			new_edge = Edge(vertex_tail_id = client.user_id,vertex_head_id = user_id)
			new_edge.save()
	
	
	if me:
		return render_to_response('vertex.html',
			{"VERTEX_DETAIL":"yourself","VERTEX_ID":user_id, "FOLLOWING_VERTEX":vertex.get_following(), "FOLLOWER_VERTEX":vertex.get_followers() },
			context_instance=RequestContext(request))
	else:
		return render_to_response('vertex.html',
			{"VERTEX_DETAIL":vertex.firstname+' '+vertex.lastname,"VERTEX_ID":user_id,"FOLLOWING_VERTEX":vertex.get_following() , "FOLLOWER_VERTEX":vertex.get_followers() },
			context_instance=RequestContext(request))
	
	return HttpResponse("You're looking at vertex %s." % vertex)

# Create your views here.
