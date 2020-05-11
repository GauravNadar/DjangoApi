from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person, PersonDetail, Signal

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']

class PersonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Person
		fields = ['name', 'gender', 'phone']
		

###############################################################################

class PersonDetailSerializer(serializers.ModelSerializer):
	#id = serializers.IntegerField(read_only=True)

	#person = PersonSerializer()

	class Meta:
		model = PersonDetail
		fields = ('person', 'salary', 'profession',)

class SignalSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Signal
		fields = ['name', 'image', 'description', 'type'] 