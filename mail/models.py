from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Mail(models.Model):
	sender=models.EmailField(max_length=254)
	subject=models.CharField(max_length=30)
	message=models.TextField(max_length=500)
	to=models.EmailField(max_length=254,unique=True)
	date_sent=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return f"{self.subject}{self.id}"

	# def save(self,*args,**kwargs):
	# 	self.author=User.objects.get(id=self.id)
	# 	super().save(*args,**kwargs)


class Search(models.Model):
	item=models.CharField(max_length=30)

	def __str__(self):
		return self.item