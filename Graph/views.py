from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from login.views import authDetail

def firstpage(request):
	if not authDetail(request)[0]:
		return render_to_response('firstpage.html',{},context_instance=RequestContext(request))
	return HttpResponseRedirect('/home/')

# Create your views here.
