from django.db import models
from django.contrib.auth.models import User

class Mail(models.Model):
	sender=models.EmailField(max_length=254)
	subject=models.CharField(max_length=30)
	message=models.TextField(max_length=500)
	to=models.EmailField(max_length=254,unique=True)


	def __str__(self):
		return f"{self.subject}{self.id}"

	# def save(self,*args,**kwargs):
	# 	self.author=User.objects.get(id=self.id)
	# 	super().save(*args,**kwargs)