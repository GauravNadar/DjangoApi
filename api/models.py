from django.db import models
from cloudinary.models import CloudinaryField

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


#for testing purposes
class TestModel(models.Model):
	test_name = models.CharField(max_length=150)
	pic = CloudinaryField('image')
	pic2 = models.BinaryField(blank=True)


	def __str__(self):
		return self.test_name



class New(models.Model):
    pic = models.ImageField(upload_to='news/')
    headline = models.CharField(max_length=500)
    priority = models.IntegerField()

    def __str__(self):
        return str(self.priority)


class Rule(models.Model):
    related_to = models.CharField(max_length=200)
    offence = models.TextField()
    penalty = models.CharField(max_length=200)
    section = models.TextField()

    def __str__(self):
        return self.offence


CORRECT_ANSWER_CHOICES = [
            ('1', 'option 1'),
            ('2', 'option 2'),
            ('3', 'option 3'),
            ('4', 'option 4')
    ]

class Question(models.Model):
    signal = models.ImageField(upload_to='question_signals/')
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500, default='null')
    option3 = models.CharField(max_length=500, default='null')
    option4 = models.CharField(max_length=500, default='null')
    correct_option = models.CharField(choices=CORRECT_ANSWER_CHOICES, max_length=100)

    def __str__(self):
        return str(self.id)

class PetrolPrice(models.Model):
    state =  models.CharField(max_length=100)
    city =  models.CharField(max_length=100)
    today_price = models.CharField(max_length=100)
    yesterday_price =  models.CharField(max_length=100)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{state} - {city}".format(state=self.state, city=self.city)

