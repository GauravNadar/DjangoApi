from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Signal, New, Rule, Question, PetrolPrice

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Group
# 		fields = ['url', 'name']

# class PersonSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Person
# 		fields = ['name', 'gender', 'phone']


# ###############################################################################

# class PersonDetailSerializer(serializers.ModelSerializer):
# 	#id = serializers.IntegerField(read_only=True)

# 	#person = PersonSerializer()

# 	class Meta:
# 		model = PersonDetail
#		fields = ('person', 'salary', 'profession',)

class SignalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Signal
		fields = ['name', 'image', 'description', 'type']



class NewsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = New
		fields = ['pic', 'headline', 'priority']


class RuleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rule
		fields = ['related_to', 'offence', 'penalty', 'section']

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Question
		fields = ['signal', 'option1', 'option2', 'option3', 'option4', 'correct_option']

class PetrolPricesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = PetrolPrice
		fields = ['state', 'city', 'today_price', 'yesterday_price']