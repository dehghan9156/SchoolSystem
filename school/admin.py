from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin



class CustomSchool(ModelAdmin):
    list_display = ["pk","name"]

class CustomClassRoom(ModelAdmin):
    list_display = ["pk","name","teacher"]


class CustomLesson(ModelAdmin):
    list_display = ["pk","name"]


class CustomNews(ModelAdmin):
    list_display = ["pk","title","lesson","created_by"]

class CustomExercise(ModelAdmin):
    list_display=["pk","title","lesson","classroom"]


admin.site.register(School,CustomSchool)
admin.site.register(Teacher_School)
admin.site.register(ClassRoom,CustomClassRoom)
admin.site.register(Lesson,CustomLesson)
admin.site.register(Studen_Lesson)
admin.site.register(News,CustomNews)
admin.site.register(Exercise,CustomExercise)