from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from login.views import authDetail
from vertex.models import *

@dajaxice_register(method = 'POST' , name = 'sayhello')
def sayhello(request,likes,do,flow_id=None):
	if do == 'like':
		flow=Flow.objects.get(id = int(flow_id))
		flow.like(likes)
		#create like codes here
		return simplejson.dumps({'message':'likes : %s'%likes})
	elif do == 'comment':
		#create comment codes here
		return simplejson.dumps({'message':'comment %s'%likes})
	elif do == 'forward':
		#create you forward codes here 
		pass
	elif do == 'falow':
		#create falow's code here
		print 'follow:',likes
		if authDetail(request)[0]:
			client = authDetail(request)[1]
			vertex = Vertex.objects.get(user_id = likes)
			try:
				new_edge = Edge.objects.get(vertex_tail_id = client.user_id,vertex_head_id = vertex.user_id)
			except:
				new_edge = Edge(vertex_tail_id = client.user_id,vertex_head_id = vertex.user_id)
				new_edge.save()
				print new_edge
			
		return simplejson.dumps({'message':""})
	elif do == 'unfollow':
		if authDetail(request)[0]:
			client = authDetail(request)[1]
			vertex = Vertex.objects.get(user_id = likes)
			try:
				new_edge = Edge.objects.get(vertex_tail_id = client.user_id,vertex_head_id = vertex.user_id).delete();
			except:
				pass
		return simplejson.dumps({'message':"unfollow"})
	print do
