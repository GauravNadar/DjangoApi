from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import UserSerializer, SignalSerializer, NewsSerializer, RuleSerializer, QuestionSerializer, PetrolPricesSerializer
from django.contrib.auth.models import User, Group
from .models import Signal, New, Rule, Question, PetrolPrice

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
from django.views.decorators.csrf import csrf_exempt

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

class PetrolPricesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PetrolPrice.objects.all()
    serializer_class = PetrolPricesSerializer

class UserList(generics.ListAPIView):
    queryset = PetrolPrice.objects.all()
    serializer_class = PetrolPricesSerializer

    def list(self, request, id):
        states = ['Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh', 'Assam','Bihar', 'Chandigarh','Chhatisgarh', 'Dadra Nagarhaveli','Daman & Diu', 'Delhi','Goa', 'Gujarat','Haryana', 'Himachal Pradesh','Jammu & Kashmir', 'Jharkhand','Karnataka', 'Kerala','Madhya Pradesh', 'Maharashtra','Manipur','Meghalaya','Mizoram', 'Nagaland','Odisha', 'Pondicherry','Punjab', 'Rajasthan','Sikkim', 'Tamil Nadu','Telangana', 'Tripura','Uttar Pradesh', 'Uttarakhand','West Bengal']
        queryset = self.get_queryset().filter(state = states[id])
        serializer = PetrolPricesSerializer(queryset, many=True)
        return Response(serializer.data)


from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View

class WebHookView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, data):
        import json
        result = json.loads(self.request.body)

        fake_result = {
				  "Gujarat": [
				    [
				      "City",
				      "Today Price",
				      "Yesterday Price"
				    ],
				    [
				      "Ahmedabad",
				      "₹ 87.76",
				      "₹ 87.72"
				    ],
				    [
				      "Amreli",
				      "₹ 89.02",
				      "₹ 89.02"
				    ],
				    [
				      "Anand",
				      "₹ 87.58",
				      "₹ 87.56"
				    ],
				    [
				      "Aravalli",
				      "₹ 88.50",
				      "₹ 88.36"
				    ]
				  ]
				}

        for key, values in result.items():
            state = key
            values.pop(0)
            for val in values:
                p = PetrolPrice.objects.filter(state=state, city=val[0])
                if p:
                    p[0].today_price = val[1]
                    p[0].yesterday_price = val[2]
                    p[0].save()
                else:
                    PetrolPrice.objects.create(state=state,
                                           city=val[0],
                                           today_price=val[1],
                                           yesterday_price=val[2])

        print(result)

        return JsonResponse(result)