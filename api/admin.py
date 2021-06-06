from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path

from .models import Signal, TestModel, New, Rule, Question, PetrolPrice

#admin.site.register(Person)
admin.site.register(Signal)
#admin.site.register(TestModel)
admin.site.register(New)
admin.site.register(Rule)
admin.site.register(Question)

class PetrolPriceAdmin(admin.ModelAdmin):
	
	def get_urls(self):
		urls = super(PetrolPriceAdmin, self).get_urls()
		my_urls = [
			path('scrape/', self.my_view, name='scrape'),
		]
		return my_urls + urls
	
	def my_view(self, request):
		# custom view which should return an HttpResponse
		print("clicked on view")
		return render(request, 'api/progress.html')
	
	change_list_template = 'api/change_list.html'
	list_display = ['state', 'city', 'today_price', 'yesterday_price', 'updated_on']

admin.site.register(PetrolPrice, PetrolPriceAdmin)
