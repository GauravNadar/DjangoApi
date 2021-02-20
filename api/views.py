from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, SignalSerializer, NewsSerializer, RuleSerializer, QuestionSerializer
from django.contrib.auth.models import User, Group
from .models import Signal, New, Rule, Question

from django.http import HttpResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

class UserViewSet(viewsets.ModelViewSet, APIView):
	#authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]


	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
# 	queryset = Group.objects.all()
# 	serializer_class = GroupSerializer

# class PersonViewSet(viewsets.ModelViewSet):
# 	queryset = Person.objects.all()
# 	serializer_class = PersonSerializer

# def TestView(request):
# 	return render(request, 'api/home.html', {"data":"data"})


# #####################################################################

# def DatatableView(request):
# 	return render(request, 'datatable/home.html')

# class PersonDetailViewSet(viewsets.ModelViewSet):
# 	queryset = PersonDetail.objects.all()
# 	serializer_class = PersonDetailSerializer


# def DatatableView(request):
# 	queryset = PersonDetail.objects.all()
# 	json = serializers.serialize('json', queryset)
# 	return HttpResponse(json, content_type='application/json')

# @csrf_exempt
# @api_view(["GET"])
# def TokenExample(request):
# 	data = {'sample_data': 123}
# 	return Response(data, status=HTTP_200_OK)


class SignalViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Signal.objects.all()
    serializer_class = SignalSerializer


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = New.objects.all()
    serializer_class = NewsSerializer


class RuleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Rule.objects.all()
    serializer_class = RuleSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer