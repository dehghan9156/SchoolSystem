from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin



class CustomSchool(ModelAdmin):
    list_display = ["pk","name"]

class CustomClassRoom(ModelAdmin):
    list_display = ["pk","name"]



admin.site.register(School,CustomSchool)
admin.site.register(Teacher_School)
admin.site.register(ClassRoom,CustomClassRoom)