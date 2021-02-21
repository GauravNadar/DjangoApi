from django.contrib import admin

from .models import Signal, TestModel, New, Rule, Question, PetrolPrice

#admin.site.register(Person)
admin.site.register(Signal)
#admin.site.register(TestModel)
admin.site.register(New)
admin.site.register(Rule)
admin.site.register(Question)
admin.site.register(PetrolPrice)
