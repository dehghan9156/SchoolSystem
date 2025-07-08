from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name="api-v1"

router = DefaultRouter()
router.register(r"admin/news",views.FullAccessNewApiView,basename="admin-news")
router.register(r"admin/exercise",views.FullAccessExerciseApiView,basename="admin-exercise")

urlpatterns = [
    path("add/school/",views.AddSchoolApiView.as_view(),name="add-school"),
    path("add/classroom/",views.AddClassRoomApiView.as_view(),name="add-classroom"),
    path("add/student/",views.AddStudentApiView.as_view(),name="add-student"),
    path("add/news/",views.AddNewsApiView.as_view(),name="add-news"),
    path("add/exercise/",views.AddExerciseApiView.as_view(),name="add-exercise"),
    path("edit/exercise/<int:pk>/",views.EditExerciseApiView.as_view(),name="edit-exercise"),
    path("edit/news/<int:pk>/",views.EditNewsApiView.as_view(),name="edit-news"),
    path("review/news/",views.ReviewsNewsApiView.as_view(),name="reviews-news"),
    path("review/exercise/",views.ReviewsExerciseApiView.as_view(),name="review-exercise"),
    path("send/exercise/<int:pk>/",views.SendExerciseApiView.as_view(),name="send-exercise"),
    path("edit/answerexercise/<int:pk>/",views.EditAnswerExercise.as_view(),name="edit-answerexercise"),
    path("",include(router.urls)),
    
]