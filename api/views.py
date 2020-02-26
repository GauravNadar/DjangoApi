from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PersonSerializer, PersonDetailSerializer
from django.contrib.auth.models import User, Group
from .models import Person, PersonDetail

from django.http import HttpResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	# permission_classes = [IsAuthenticated]

	# def get(self, request, format=None):
	# 	content = {
	# 	'user': unicode(request.user),
	# 	'auth': unicode(request.auth),
	# 	}
	# 	return Response(content)

	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet, APIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

def TestView(request):
	return render(request, 'api/home.html', {"data":"data"})


#####################################################################

def DatatableView(request):
	return render(request, 'datatable/home.html')

class PersonDetailViewSet(viewsets.ModelViewSet):
	queryset = PersonDetail.objects.all()
	serializer_class = PersonDetailSerializer


# def DatatableView(request):
# 	queryset = PersonDetail.objects.all()
# 	json = serializers.serialize('json', queryset)
# 	return HttpResponse(json, content_type='application/json')
