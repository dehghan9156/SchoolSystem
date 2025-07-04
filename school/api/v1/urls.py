from django.contrib import admin
from django.urls import path,include
from . import views

app_name="api-v1"

urlpatterns = [
    path("add/school/",views.AddSchoolApiView.as_view(),name="add-school"),
    path("add/classroom/",views.AddClassRoomApiView.as_view(),name="add-classroom"),
    path("add/student/",views.AddStudentApiView.as_view(),name="add-student"),

]