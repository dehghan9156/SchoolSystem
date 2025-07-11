from django.contrib import admin
from django.urls import path,include
from . import views
app_name="api-v1"

urlpatterns = [
    path("get/message/<int:room_id>/",views.GetMessageApiView.as_view(),name="websocket-consumer"),
    path("get/message/teacher/",views.GetMessageTeacherApiView.as_view(),name="get-message-teacher"),
]