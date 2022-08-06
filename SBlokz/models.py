from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.utils.html import escape, mark_safe
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

class User(AbstractUser):
	is_manufacturer = models.BooleanField(default=False)
	is_retailer = models.BooleanField(default=False)

class Friend(models.Model):
	users = models.ManyToManyField(User)
	current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

	@classmethod
	def make_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user=current_user
		)
		friend.users.add(new_friend)

	@classmethod
	def lose_friend(cls, current_user, new_friend):
		friend, created = cls.objects.get_or_create(
			current_user=current_user
		)
		friend.users.remove(new_friend)



class Order(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	hash_id = models.CharField(max_length=100, default=uuid.uuid4())
	date_ordered = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('manu-detail', kwargs={'pk': self.pk})




class Product(models.Model):
	title = models.CharField(max_length=100)
	producttype = models.CharField(max_length=50)
	content = models.TextField()
	hash_id = models.CharField(max_length=100, default=uuid.uuid4())
	date_product = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('manu-detail_product', kwargs={'pk': self.pk})