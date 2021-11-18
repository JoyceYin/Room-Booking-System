from django.db import models

# Create your models here.

class user_id(models.Model):
	UID = models.IntegerField(unique=True)
	name = models.CharField(max_length=200, unique=True)
	email = models.EmailField(max_length = 40, default=0)
	password = models.CharField(max_length = 30)

	def __str__(self):
		return self.name
	
	
class book(models.Model):
	UID = models.IntegerField()
	RID = models.IntegerField()
	book_id = models.IntegerField(unique = True)
	indate = models.DateTimeField()

class wishlist(models.Model):
	UID = models.IntegerField()
	RID = models.IntegerField()