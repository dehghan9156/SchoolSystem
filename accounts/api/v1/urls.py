from django.contrib import admin
from django.urls import path,include
from . import views


app_name="api-v1"

urlpatterns = [
    path("register/<str:role>/",views.UserRegisterApiView.as_view(),name='user-register'),

]