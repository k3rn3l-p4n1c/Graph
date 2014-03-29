from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from vertex.models import Vertex,Edge,Flow
import json
from django.utils import timezone

   
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
    
    #flows = client.flow_set.order_by('-last_forward_date')[:5] 
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
			{"VERTEX_DETAIL":"yourself","VERTEX_ID":user_id, "FOLLOWING_VERTEX":vertex.get_following(), "FOLLOWER_VERTEX":vertex.get_followers(), },
			context_instance=RequestContext(request))
	else:
		return render_to_response('vertex.html',
			{"VERTEX_DETAIL":vertex.firstname+' '+vertex.lastname,"VERTEX_ID":user_id,"FOLLOWING_VERTEX":vertex.get_following() , "FOLLOWER_VERTEX":vertex.get_followers(), },
			context_instance=RequestContext(request))
	
	return HttpResponse("You're looking at vertex %s." % vertex)
def postflow(request,user_id):
    flow_text = request.POST['flow_text']
    pub_date = timezone.now()
    newflow = Flow.objects.create(text = flow_text,pub_date = timezone.now(),last_forward_date = timezone.now(),owner = user_id)
    vertex = Vertex.objects.get(user_id = user_id)
    newflow.set_history(vertex.user_id)
    newflow.save()
    vertex.flow_set.add(newflow)
    #gotta add others too
    
    
def forward(request,user_id):
    flow_text = request.POST['flow_text']
    forward_to = request.POST['forward_to']
    flow = Flow.objects.get(text = flow_text)
    flow.last_forward_date = timezone.now()
    flow.save()
    vertex = Vertex.objects.get(user_id = user_id)
    if forward_to == "all":
        followers_list = vertex.get_followers()
        for followers in followers_list:
            followers.flow_set.add(flow)
            followers.save()
    else:
        forward_list = [] #I'll change it later with the html
        for index,followers in enumerate(forward_list):
            follower = Vertex.objects.get(user_id = followers)
            follower.flow_set.add(flow)
            follower.save()
            
            
        
    
def like_flow(request,liker_id):
    flow_text = request.POST['flow_text']
    flow = Flow.objects.get(text = flow_text)
    flow.like(liker_id)
    flow.save()
    
    
# Create your views here.
