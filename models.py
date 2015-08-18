from django.db import models
import datetime

class getData(models.Model):
	account_num = models.IntegerField(default=0)
	name = models.CharField(max_length= 200)
	street_address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=200)
	zipcode = models.IntegerField(default=0)
	timestamp = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return '%s, %s, %s %s, %s' %(self.name, self.street_address, self.city, self.state, self.zipcode)
