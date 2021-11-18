from django.http import HttpResponse
from django.shortcuts import render

import datetime

def HomePage(request):
	today = datetime.datetime.now().date()
	content = {"title": "UBooking", "today": today}
	return render(request, "home.html", content)
