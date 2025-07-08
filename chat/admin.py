from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin

class CustomChatroom(ModelAdmin):
    list_display =["pk","name"]
 
class CustomMessage(ModelAdmin):
    list_display =["pk","sender","content","chatroom","timestamp"]
 

admin.site.register(Chatroom,CustomChatroom)
admin.site.register(Message,CustomMessage)
 