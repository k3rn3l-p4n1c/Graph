from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse
   
def firstpage(request):
	return render_to_response('firstpage.html', context_instance=RequestContext(request))

# Create your views here.
