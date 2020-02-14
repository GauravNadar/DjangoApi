from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Person

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
		feilds = ['name', 'gender']
		