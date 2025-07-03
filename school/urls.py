from django.contrib import admin
from django.urls import path,include

app_name="school"

urlpatterns = [
    path("api/v1/",include("school.api.v1.urls",namespace="api-v1")),
]