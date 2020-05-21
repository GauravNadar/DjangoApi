from django.db import models

# DESIGNATION_CHOICES = [
# 		('d','Doctor'),
# 		('e', 'Engineer'),
# 		('o', 'Others'),
# 	]

# class Person(models.Model):

# 	GENDER_CHOICES = [
# 		('m','Male'),
# 		('f', 'Female'),
# 		('o', 'Others'),
# 	]

	

# 	name = models.CharField(max_length=50)
# 	gender = models.CharField(choices=GENDER_CHOICES, max_length=50)
# 	phone = models.IntegerField()

# 	def __str__(self):
# 		return self.name


# class PersonDetail(models.Model):
# 	person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='details', verbose_name='name')
# 	salary = models.IntegerField()
# 	profession = models.CharField(choices=DESIGNATION_CHOICES, max_length=50)


# 	def __str__(self):
# 		return self.person.name


class Signal(models.Model):
	name = models.CharField(max_length=150)
	image = models.ImageField(upload_to='symbols/')
	description = models.TextField()
	type = models.CharField(max_length=50)


	def __str__(self):
		return self.name

