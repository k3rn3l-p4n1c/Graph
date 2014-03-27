from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from vertex.models import Vertex,Edge,Friends,Flow
from Django.utils import timezone

   
def profile(request, user_id):
	try:
		vertex = Vertex.objects.get(user_id=user_id)
        fname = vertex.firstname
        lname = vertex.lastname
        flowlist = vertex.flow_set.all()
        vertex_friends = Friends.objects.get(name = user_id+'_friends')
	except :
		return render_to_response('404error.html',
			{},
			context_instance=RequestContext(request))
	client = None
	try:
		eml = request.COOKIES[ 'email' ]
		pwd = request.COOKIES[ 'password' ]
        client = Vertex.objects.get(email = eml)
        fname = vertex.firstname
        lname = vertex.lastname
        flowlist = vertex.flow_set.order_by('-pub_date')[:5] 
        vertex_friends = Friends.objects.get(name = user_id+'_friends')
		if client.password != pwd:
			raise LookupError()
	except:
		client = None

	context = {'fname' = fname,'lname'=lname,'flowlist'=flowlist,'vertex_friends' = vertex_friends}
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
	
	return HttpResponse("You're looking at vertex %s." % vertex) #making a home page template like facebook home

def flow(request,user_id):
    vertex = Vertex.objects.get(user_id=user_id)
    fname = vertex.firstname
    lname = vertex.lastname
    vertex_friends = Friends.objects.get(name = userid+'_friends')
    flowtext = request.POST['flowtext']
    newflow = FLow.objects.create(text = flowtext,pub_date = timezone.now())
    newflow.save()
    for i in vertex_friends.members.all(): #for now to all....I'll put a choice system later
        i.flow_set.add(newflow)
        i.save()
    

# Create your views here.
