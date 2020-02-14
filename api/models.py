from django.db import models

class Person(models.Model):

	GENDER_CHOICES = [
		('m','Male'),
		('f', 'Female'),
		('o', 'Others'),
	]
	name = models.CharField(max_length=50)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
	phone = models.IntegerField()

	def __str__(self):
		return self.name
