"""rapidapipractice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet, PersonViewSet, TestView, DatatableView, PersonDetailViewSet
from rest_framework.authtoken import views as rest_auth_view

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'person', PersonViewSet)
router.register(r'data', PersonDetailViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('test/', TestView, name='test'),

    path('datatable/', DatatableView, name='datatable'),

    path('get-token/', rest_auth_view.obtain_auth_token, name='get-token'),
]
