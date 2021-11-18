from django.urls import path
from . import views
#from .models import room_info
# Create your views here.


urlpatterns = [
	path('<RID>/', views.detail),
]