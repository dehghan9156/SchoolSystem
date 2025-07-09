from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name="api-v1"

urlpatterns = [
    path('register/<str:role>/',views.UserRegisterApiView.as_view(),name='user-register'),
    path('login/<str:role>/',views.UserLoginApiView.as_view(),name='user-login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',views.UserLogoutApiView.as_view(),name='user_logout'),
    path('edit/profile/',views.EditProfileApiView.as_view(),name='edit-profile'),
    path('get/users/',views.GetUsersApiView.as_view(),name='get-users'),
    path('user/confirm/<int:pk>/',views.UserConfirmApiView.as_view(),name='user-confirm'),
    
]