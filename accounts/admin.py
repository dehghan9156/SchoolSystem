from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from accounts.models import * 

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['name','family','role','confirmation']



admin.site.register(User,CustomUserAdmin)