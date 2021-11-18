from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class users(models.Model):

	usertype = (
		('1', 'booker'),
		('2', 'host'),
		)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 40)
    #sex = models.CharField(max_length=32, choices=gender, default="Male")
	#year = models.IntegerField()
	c_time = models.DateTimeField(default=timezone.now)
	usertype = models.CharField(max_length=32, choices=usertype, default="1")

	def __str__(self):
		return self.username



