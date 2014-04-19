from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register(method = 'POST' , name = 'sayhello')
def postit(request,likes,do):
	pass
