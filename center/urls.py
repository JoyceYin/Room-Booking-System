from django.urls import path
from django.conf.urls import url
from .import views
# Create your views here.
from django.urls import path, include
urlpatterns = [
	path('', views.center),
	path('delete/<id>', views.delete),
    
]