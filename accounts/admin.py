from django.contrib import admin
from django.contrib.admin import ModelAdmin
from accounts.models import * 

class CustomUser(ModelAdmin):
    list_display = ['name','family','role','confirmation']



admin.site.register(User,CustomUser)