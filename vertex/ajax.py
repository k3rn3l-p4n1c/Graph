from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

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
		pass