from django.urls import path
from . import views
from django.conf.urls import url
# Create your views here.

urlpatterns = [
	path('', views.login, name = ''),
	path('register', views.register),
	url(r'^logout/', views.logout),
]