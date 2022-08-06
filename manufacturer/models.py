from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):

	manu = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=False)

	image = models.ImageField(default='user.jpg,', upload_to='profile_pics')
	
	

	def __str__(self):
		return f'{self.manu.username} Profile'


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)


		img = Image.open(self.image.path)


		if img.height>300 or img.width>300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

