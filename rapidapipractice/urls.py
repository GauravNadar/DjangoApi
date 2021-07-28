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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import UserViewSet, SignalViewSet, NewsViewSet, RuleViewSet, QuestionViewSet, PetrolPricesViewSet, WebHookView, UserList, PrivacyPolicyView
from rest_framework.authtoken import views as rest_auth_view

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
#router.register(r'person', PersonViewSet)
#router.register(r'data', PersonDetailViewSet)
router.register(r'signals', SignalViewSet)
router.register(r'news', NewsViewSet)
router.register(r'rules', RuleViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'petrol-prices', PetrolPricesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('test/', TestView, name='test'),

    #path('datatable/', DatatableView, name='datatable'),

    path('get-token/', rest_auth_view.obtain_auth_token, name='get-token'),

    #path('token-example/', TokenExample, name='token-example'),
    path('webhook/', WebHookView.as_view(), name='webhook'),
	
	path('list/<int:id>', UserList.as_view(), name='user-list')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
