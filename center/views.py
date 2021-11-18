from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .form import SubmitForm
from .models import book,user_id,wishlist
from search.models import update
from login.models import users
from detail.models import room_info
from search.models import listing
import random
from django.core import serializers

import json


def center(request,type):
	#usertype = users.objects.get(usertype = '1')
	#usertype = request.GET.get("usertype",None)
	#user = users.objects.get(usertype=usertype)
	if type=="booker":    
		UID=request.session.get('bookid')
		user = user_id.objects.filter(UID=UID)[0]
		lists = book.objects.filter(UID=UID).extra(
select={'street':'search_listing.street','RID':'search_listing.RID'},
tables=['search_listing'],
where=['search_listing.RID=center_book.RID']
)
		room = book.objects.filter(UID=UID).extra(
select={'pic':'detail_room_info.image_url','name':'detail_room_info.name'},
tables=['detail_room_info'],
where=['detail_room_info.RID=center_book.RID']
) 
		wish = wishlist.objects.filter(UID = UID).extra(
			select = {'RID':'center_wishlist.RID','street':'search_listing.street','name':'detail_room_info.name','pic':'detail_room_info.image_url'},
			tables = ['search_listing','detail_room_info'],
			where = ['search_listing.RID = center_wishlist.RID','detail_room_info.RID = center_wishlist.RID']
			)

		lists=list(lists)
		room=list(room)
		listings=zip(lists,room)                                   
		return render(request, "usercenter.html", {"title": "Booker Center","user":user,"listings":listings,"wish":wish})



	if type=="host":
		HID=request.session.get('hostid')
		lists = listing.objects.filter(HID = HID).extra(
			select={'RID':'search_listing.RID','name':'detail_room_info.name','description':'search_listing.description','street':'search_listing.street','pic':'detail_room_info.image_url','price':'detail_room_info.price'},
			tables=['detail_room_info'],
			where=['search_listing.RID=detail_room_info.RID']
			)

		if request.method == "POST":
			form = SubmitForm(request.POST)
			print(request.POST)
		
			name = request.POST.get("name",None)
			street = request.POST.get("street", None)
			type = request.POST.get("type", None)
			accommodates = request.POST.get("accommodates", None)
			bathrooms = request.POST.get("bathrooms", None)
			bedrooms = request.POST.get("bedrooms", None)
			amenities = request.POST.get("amenities", None)
			price = request.POST.get("price", None)
			url = request.POST.get("url", None)
			HID = request.session.get('hostid')
			description = request.POST.get("description", None)
			country = request.POST.get("country",None)
			
			new_room = room_info()
			new_room.RID = random.randint(400000,8000000)
			new_room.name = name
			new_room.type = type
			new_room.accommodates = accommodates
			new_room.stars = 5
			new_room.bathrooms = bathrooms
			new_room.bedrooms = bedrooms
			new_room.amenities = amenities
			new_room.price = price
			new_room.image_url = url
			new_room.save()
			
			new_room1 = listing()
			new_room1.RID = new_room.RID
			new_room1.street = street+','+country
			new_room1.description = description
			new_room1.HID = HID
			new_room1.save()
			message = "Submit Successfully!"
			return render(request, 'hostcenter.html', {'form': form, 'message': message, "title": "Host Center","lists":lists})
		else:
		#return HttpResponse("fail");
			form = SubmitForm()

		return render(request, "hostcenter.html", {'form': form,"title": "Host Center","lists":lists})
	



def delete(request,type,id):
	if type=="booker":       
		UID=request.session.get('bookid')
		dingdan=book.objects.get(UID=UID)
		listing.objects.filter(RID=dingdan.RID).update(statement='1')
		book.objects.filter(id=id).delete()
		
		return HttpResponseRedirect("/center/booker")
	

	
