from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import os

# Create your models here.
class room_info(models.Model):
	RID = models.IntegerField(unique = True)
	name = models.CharField(max_length = 100)
	type = models.CharField(max_length = 25)
	accommodates = models.IntegerField()
	stars = models.DecimalField(max_digits = 3, decimal_places = 1)
	bathrooms = models.IntegerField()
	bedrooms = models.IntegerField()
	amenities = models.TextField()
	price = models.IntegerField()
	image_url = models.URLField(default = ' ', blank = True)

	def __str__(self):
		return self.RID

	def get_remote_image(self):
		if self.image_url:
			result = urllib.urlretrieve(self.image_url)
			self.image_url.save(
				os.path.basename(self.image_url),
				File(open(result[0]))
				)
			self.save()


class rating(models.Model):
	RID = models.IntegerField()
	UID = models.IntegerField()
	comments = models.TextField()

