from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .form import BookForm
from .models import room_info,rating
from search.models import host_info, listing
from center.models import book, wishlist
from login.models import users
import random
# Create your views here.

def detail(request, RID):
	RID = RID
	RID_record = room_info.objects.filter(RID=RID).extra(
		select={'hostname':'search_host_info.name','about':'search_host_info.about','email':'search_host_info.email','location':'search_listing.street','HID':'search_host_info.HID'},
		tables=['search_listing','search_host_info'],
		where=['detail_room_info.RID=search_listing.RID', 'search_listing.HID=search_host_info.HID']
	)

	message = ' '

	review=rating.objects.filter(RID=RID).extra(
	select=
{'name':'center_user_id.name'},tables=['center_user_id'],where=['center_user_id.UID=detail_rating.UID'])


	form = BookForm(request.POST)
	#if visitor(no account)
	if not request.session.get('username'):
		message = "All details only available for users!"
		return HttpResponseRedirect("/login/")



	if request.method == "POST":

		if form.is_valid():
			indate = request.POST.get("indate") #work
			book_RID = RID
			book_UID = request.session.get('bookid')

			if indate == "": 
				message = "Choose an Arrival Date First!"
				return render(request, 'roomdetail.html', {'form': form, 'message': message, "title": "About Room!","RID_record": RID_record})
			else:
				new_book = book()
				new_book.RID = book_RID
				new_book.UID = book_UID
				new_book.indate = indate
				new_book.book_id = random.randint(200000,500000)
				new_book.save()
				listing.objects.filter(RID=book_RID).update(statement='2')
				message = "Reserve Successfully!"
				return render(request, 'roomdetail.html', {'form': form, 'message': message, "title": "About Room!","RID_record": RID_record})
	
	else:
		form = BookForm()
	return render(request, 'roomdetail.html', {'form': form,"title": "About Room!","RID_record": RID_record,"review":review})