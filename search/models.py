from django.db import models
import django.utils.timezone as timezone
from django.core.files import File
import os

# Create your models here.
	
class host_info(models.Model):
	HID = models.IntegerField(unique = True)
	name = models.CharField(max_length = 200, unique=True)
	about = models.TextField(default='Nothing')
	email = models.EmailField(max_length = 40)
	password = models.CharField(max_length = 30)
	image_url = models.URLField(default = ' ', blank = True)
	statement = models.IntegerField(default = 1)

	def get_remote_image(self):
		if self.image_url:
			result = urllib.urlretrieve(self.image_url)
			self.image_url.save(
				os.path.basename(self.image_url),
				File(open(result[0]))
				)
			self.save()

	def __str__(self):
		return self.name


class listing(models.Model):
	HID = models.IntegerField()
	RID = models.IntegerField(unique = True)
	street = models.CharField(max_length=500)
	description = models.CharField(max_length=1000, default='Nothing')
	statement = models.IntegerField(default = 1)  
	review_num = models.IntegerField(default = 0) 
	def __str__(self):
		return self.RID
	


class update(models.Model):
	AID = models.IntegerField(unique = True)
	RID = models.IntegerField(unique = True)
	update_id = models.IntegerField(unique = True)