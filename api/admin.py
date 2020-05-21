from django.contrib import admin

from .models import Signal, TestModel

#admin.site.register(Person)
admin.site.register(Signal)
admin.site.register(TestModel)
