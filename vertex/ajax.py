from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from login.views import authDetail
from vertex.models import Edge,Vertex

@dajaxice_register(method = 'POST' , name = 'sayhello')
def sayhello(request,likes,do):
	if do == 'like':
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
		print request
		if authDetail(request)[0] and False:
			client = authDetail(request)[1]
			vertex = Vertex.objects.get()
			try:
				new_edge = Edge.objects.get(vertex_tail_id = client.user_id,vertex_head_id = vertex.user_id)
			except:
				new_edge = Edge(vertex_tail_id = client.user_id,vertex_head_id = vertex.user_id)
				new_edge.save()
			
		return simplejson.dumps({'message':""})
