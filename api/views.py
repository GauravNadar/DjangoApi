from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PersonSerializer
from django.contrib.auth.models import User, Group


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer