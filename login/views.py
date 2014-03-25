from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect

def view(request):
	return render_to_response('firstpage.html', context_instance=RequestContext(request))

def login(request):
	try:
		eml = request.POST['email']
		pwd = request.POST['password']
	except :
		return HttpResponse('Error')
	response = HttpResponseRedirect('/home/')
  	response.set_cookie( 'email' , eml )
  	response.set_cookie( 'password' , pwd)
  	return response

def logout(request):
	response = HttpResponseRedirect('/')
	response.delete_cookie('email')
	response.delete_cookie('password')
	return response
    
# Create your views here.
