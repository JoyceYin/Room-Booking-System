from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.core import serializers
import datetime
# Create your views here.
from .models import listing, host_info
from detail.models import room_info 
import json


#def index(request):
#	today = datetime.datetime.now().date()
#	return render(request, "hello.html", {"today": today})

def search(request):
	pass
	return render(request, "searchlisting.html", {"title": "Explore More!"})


def cheap(request,country):

	listings = listing.objects.filter(street__contains=country,statement=1).extra(
select={'name':'detail_room_info.name','pic':'detail_room_info.image_url','rating':'detail_room_info.stars','price':'detail_room_info.price'},
tables=['detail_room_info'],
where=['search_listing.RID=detail_room_info.RID']
).order_by('price')

	paginator = Paginator(listings, 10)

	page = request.GET.get('page')

	listings = paginator.get_page(page)

	return render(request, "searchlisting.html", {"title": "Explore More!", "listings": listings ,"country":country})

def review(request,country):

	listings = listing.objects.filter(street__contains=country,statement=1).extra(
select={'name':'detail_room_info.name','pic':'detail_room_info.image_url','rating':'detail_room_info.stars','price':'detail_room_info.price'},
tables=['detail_room_info'],
where=['search_listing.RID=detail_room_info.RID']).order_by('-review_num')
  
	paginator = Paginator(listings, 10)

	page = request.GET.get('page')

	listings = paginator.get_page(page)

	return render(request, "searchlisting.html", {"title": "Explore More!", "listings": listings ,"country":country})

def popular(request,country):

	listings = listing.objects.filter(street__contains=country,statement=1).extra(
select={'name':'detail_room_info.name','pic':'detail_room_info.image_url','rating':'detail_room_info.stars','price':'detail_room_info.price'},
tables=['detail_room_info'],
where=['search_listing.RID=detail_room_info.RID']
).extra(order_by = ['-rating'])
  
	paginator = Paginator(listings, 10)

	page = request.GET.get('page')

	listings = paginator.get_page(page)

	return render(request, "searchlisting.html", {"title": "Explore More!", "listings": listings ,"country":country})

def listout(request,country):

	listings = listing.objects.filter(street__contains=country,statement=1).extra(
select={'name':'detail_room_info.name','pic':'detail_room_info.image_url','rating':'detail_room_info.stars','price':'detail_room_info.price'},
tables=['detail_room_info'],
where=['search_listing.RID=detail_room_info.RID']
)
	listings=listings
	paginator = Paginator(listings, 10)

	page = request.GET.get('page')

	listings = paginator.get_page(page)

	return render(request, "searchlisting.html", {"title": "Explore More!", "listings": listings ,"country":country})


def success(request):
	newslist = []
	newslist.append([1,'Data Processing Workshop I Quiz finished','2020-5-1','Rui'])
	newslist.append([2,'Data Processing Workshop I Project Released','2020-5-4','Qian'])
	newslist.append([3,'Data Processing Workshop I Quiz Grade Released','2020-5-7','Changjiang'])
	newslist.append([4,'Data Processing Workshop I Assignment Released','2020-5-10','Jie'])
	today = datetime.datetime.now().date()
	return render(request, "success.html", {"newslist": newslist, "date": today})
