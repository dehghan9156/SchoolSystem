from django.contrib import admin
from django.urls import path,include
from . import views

app_name="api-v1"

urlpatterns = [
    path("add/school/",views.AddSchoolApiView.as_view(),name="add-school"),
    path("add/classroom/",views.AddClassRoomApiView.as_view(),name="add-classroom"),
    path("add/student/",views.AddStudentApiView.as_view(),name="add-student"),
    path("add/news/",views.AddNewsApiView.as_view(),name="add-news"),
    path("add/exercise/",views.AddExerciseApiView.as_view(),name="add-exercise"),
    path("edit/exercise/<int:pk>/",views.EditExerciseApiView.as_view(),name="edit-exercise"),
    path("edit/news/<int:pk>/",views.EditNewsApiView.as_view(),name="edit-news"),
]