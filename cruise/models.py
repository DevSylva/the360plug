from django.db import models


# Create your models here.
class Message(models.Model):
	name = models.CharField(max_length=40, null=True, blank=False)
	emailAddress = models.EmailField(max_length=250, null=True, blank=False)
	phoneNumber = models.CharField(max_length=15, null=True, blank=False)
	message = models.TextField(max_length=1000, null=True, blank=False)
	seen = models.BooleanField(default=False, null=True)

	def __str__(self):
		return str(self.name)

class Business(models.Model):
	product = models.CharField(max_length=50, null=True)
	cost = models.CharField(max_length=10, null=True, blank=False)

	def __str__(self):
		return str(self.product)