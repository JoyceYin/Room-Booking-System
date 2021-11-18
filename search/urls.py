from django.urls import path

from . import views
# Create your tests here.

urlpatterns = [
	path('', views.search),

   path('<country>', views.listout, name="country"),
   path('<country>/cheap', views.cheap),
   path('<country>/popular', views.popular),
   path('<country>/Review', views.review),
]