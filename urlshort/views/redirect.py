from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from urlshort.models.urlshort import Urlshortadd

def urlredirect(request,keyword):	
    try:
    	data = Urlshortadd.objects.get(keyword=keyword)
    	return redirect(data.original_url)
    except:
    	raise Http404('Sorry the link is broken :(')