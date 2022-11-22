from django.contrib import admin

from .models import *

class ExercicesFilter(admin.ModelAdmin):
    list_display = ("id", "debut", "fin", "initiateur", "etat")
    list_filter  = ("etat",)
    
# Register your models here.
admin.site.register(Exercice, ExercicesFilter)