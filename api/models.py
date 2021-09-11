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

QUIZ_CORRECT_CHOICES = [
            ('1', 'option 1'),
            ('2', 'option 2'),
            ('3', 'option 3')
    ]

MAINTENANCE_PRIORITY_CHOICES = [
            ('1', 'High'),
            ('2', 'Medium'),
            ('3', 'Low')
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
    today_price = models.CharField(max_length=100, null=True)
    yesterday_price =  models.CharField(max_length=100, null=True)
    updated_on = models.DateTimeField(null=True)
    diesel_today_price = models.CharField(max_length=100, null=True)
    diesel_yesterday_price = models.CharField(max_length=100, null=True)
    diesel_updated_on = models.DateTimeField(null=True)

    def __str__(self):
        return "{state} - {city}".format(state=self.state, city=self.city)
    
class Quiz(models.Model):
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500, default='null')
    option3 = models.CharField(max_length=500, default='null')
    correct_option = models.CharField(choices=QUIZ_CORRECT_CHOICES, max_length=100)

    def __str__(self):
        return str(self.id)
    
class MaintenanceActivity(models.Model):
    priority = models.CharField(choices=MAINTENANCE_PRIORITY_CHOICES, max_length=100)
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=500)
    message = models.TextField()
    app_update_required = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

