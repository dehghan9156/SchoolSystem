from django.contrib import admin
from django.urls import path,include

app_name="chat"

urlpatterns = [
    path("api/v1/",include("chat.api.v1.urls",namespace="api-v1")),
]