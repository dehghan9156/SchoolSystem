from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin



class CustomSchool(ModelAdmin):
    list_display = ["pk","name"]

class CustomTeacher_school(ModelAdmin):
    list_display=["pk","teacher","school"]



class CustomClassRoom(ModelAdmin):
    list_display = ["pk","name","teacher"]


class CustomLesson(ModelAdmin):
    list_display = ["pk","name"]


class CustomNews(ModelAdmin):
    list_display = ["pk","title","lesson","created_by"]

class CustomExercise(ModelAdmin):
    list_display=["pk","title","lesson","classroom"]

class CustomClassRoom_Student(ModelAdmin):
    list_display = ["pk","student","classroom"]

class CustomStudent_Lesson(ModelAdmin):
    list_display = ["pk","student","lesson"]

class CustomAnswerExercise(ModelAdmin):
    list_display = ["pk","exercise","student","submited_date"]


admin.site.register(School,CustomSchool)
admin.site.register(Teacher_School,CustomTeacher_school)
admin.site.register(ClassRoom,CustomClassRoom)
admin.site.register(Lesson,CustomLesson)
admin.site.register(Studen_Lesson,CustomStudent_Lesson)
admin.site.register(News,CustomNews)
admin.site.register(Exercise,CustomExercise)
admin.site.register(ClassRoom_Student,CustomClassRoom_Student)
admin.site.register(AnswerExercise,CustomAnswerExercise)