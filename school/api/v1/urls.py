from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name="api-v1"


router = DefaultRouter()
router.register(r"admin/news",views.FullAccessNewApiView,basename="admin-news")
router.register(r"admin/exercise",views.FullAccessExerciseApiView,basename="admin-exercise")
router.register(r"admin/lesson",views.FullAccessLessonApiView,basename="admin-lesson")
router.register(r"admin/classroom",views.FullAccessClassroomApiView,basename="admin-classroom")
router.register(r"news/filter",views.NewsFilterApiView,basename="news-filter")
router.register(r"review/news",views.ReviewsNewsApiView,basename="review-news")


urlpatterns = [
    path("add/school/",views.AddSchoolApiView.as_view(),name="add-school"),
    path("add/teacher/to/school/",views.AddTeacherToschoolApiView.as_view(),name="add-teacher-to-school"),
    path("add/student/",views.AddStudentApiView.as_view(),name="add-student"),
    path("add/news/",views.AddNewsApiView.as_view(),name="add-news"),
    path("add/exercise/",views.AddExerciseApiView.as_view(),name="add-exercise"),
    path("edit/exercise/<int:pk>/",views.EditExerciseApiView.as_view(),name="edit-exercise"),
    path("edit/news/<int:pk>/",views.EditNewsApiView.as_view(),name="edit-news"),
    # path("review/news/",views.ReviewsNewsApiView.as_view(),name="reviews-news"),
    path("review/exercise/",views.ReviewsExerciseApiView.as_view(),name="review-exercise"),
    path("send/exercise/<int:pk>/",views.SendExerciseApiView.as_view(),name="send-exercise"),
    path("edit/answerexercise/<int:pk>/",views.EditAnswerExercise.as_view(),name="edit-answerexercise"),
    path("",include(router.urls)),
    path("review/lesson/",views.ReviewLessonaApiView.as_view(),name="review-lesson"),
    path("lessons/public/",views.LessonPublicApiView.as_view(),name="lessons-public"),
    path("add/user/classroom/<int:pk>/",views.AddUserClassRoom.as_view(),name="add-user-classroom"),
    path("find/school/",views.FindNearestSchoolApiView.as_view(),name="find-nearest-school"),
    path("show/logs/",views.ShowLogsApiView.as_view(),name="show-logs"),
]