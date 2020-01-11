from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import F
from urlshortener import models
from django.views.decorators.csrf import csrf_exempt
from ratelimit.decorators import ratelimit

# Create your views here.

@ratelimit(key='ip', rate='100/h')
@csrf_exempt
def index(request):

	if  request.method == "POST":
		link_db = models.Link()
		link_db.link = request.POST.get("url").strip()
		link_db.save()
		short_url = request.POST.get("short", None)
		if short_url is None or len(short_url.strip())==0:
			short_url = link_db.get_short_id()
		else:
			try:
				item = models.Link.objects.get(short=short_url) 
			except:
				item = None
			if item is not None: 
				return render(request, "index.html",
				{'generic_text':"This short URL ",
				'link':'already exists!',
				'url_shortened':False})

			short_url = short_url.strip()

		link_db.short = short_url
		link_db.save()
		return render(request, "index.html",
			{'generic_text':request.build_absolute_uri()+'short/',
			'link':short_url,
			'url_shortened':True})

	return render(request, 'index.html', {
		'generic_text': 'How are ',
		'link': 'you!',
		'url_shortened':False
		})

@ratelimit(key='ip', rate='100/h')
def link(request, id):
	link_db = get_object_or_404(models.Link, short=id)
	if link_db.is_expired(): 
		link_db.delete()
		return render(request, 'index.html', {
			'generic_text': 'This link has expired ',
			'link': 'and is now deleted!',
			'url_shortened':False
			})
	models.Link.objects.filter(short=id).update(hits=F('hits')+1)
	return redirect(link_db.link)