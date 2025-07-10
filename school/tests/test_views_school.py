import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from school.models import *

User = get_user_model()


@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def user_teacher():
    user = User.objects.create_user(username="teach",password="123",role="teacher")
    return user

@pytest.fixture
def user_student():
    user = User.objects.create_user(username="1234566655",password="123",role="student")
    return user

@pytest.mark.django_db
class TestGetApi:
    def test_get_news(self,api_client,user_teacher):
        api_client.force_authenticate(user=user_teacher)
        url = reverse("school:api-v1:add-news")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_get_exercise(self,api_client,user_teacher):
        url = reverse("school:api-v1:add-exercise")
        api_client.force_authenticate(user=user_teacher)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_get_retrive_news(self,api_client,user_student):
        url = reverse("school:api-v1:reviews-news")
        api_client.force_authenticate(user=user_student)
        response = api_client.get(url)
        assert response.status_code == 200

 
 
@pytest.mark.django_db
class TestPostApi:
    
    def test_post_add_student(self,api_client,user_teacher):
        url = reverse("school:api-v1:add-student")
        api_client.force_authenticate(user=user_teacher)
        data = {
            "codemeli":"7894563652"
        }
        response = api_client.post(url,data)
        response.status_code == 200
    
    def test_post_add_news(self,api_client,user_teacher):
        url = reverse("school:api-v1:add-news")
        user_admin = User.objects.create(username="admin",password="123",role="admin")
        api_client.force_authenticate(user=user_admin)
        school = School.objects.create(name="s1")

        api_client.force_authenticate(user=user_teacher)
        l1 = Lesson.objects.create(name="l1")
        c1 = ClassRoom.objects.create(name="c1",teacher=user_teacher,school=school)
        data={
            "title": "test",
            "text": "eeeeee",
            "lesson": l1,
            "classroom": c1
        }
        response = api_client.post(url,data)
        print(response.data)
        assert response.data["lesson"] == "l1"



@pytest.mark.django_db
class TestPutApi:

    def test_put_edit_answerexercise(self,api_client,user_student,user_teacher):
        api_client.force_authenticate(user=user_teacher)
        lesson = Lesson.objects.create(name="l1")
        school = School.objects.create(name="s1") 
        classroom = ClassRoom.objects.create(name="c1",teacher=user_teacher,school=school)       
        exercise = Exercise.objects.create(
            title= "wwwwwwwwwwwwww",
            content= "qqqqqqq",
            deadline= "2025-07-07T15:22:16+03:30",
            lesson=lesson,
            classroom= classroom,
            created_by = user_teacher
    
        )
        answer_exercise = AnswerExercise.objects.create(
            exercise=exercise,
            student=user_student,
            answer_text ="jndjnwfmw"
        )
        url = reverse("school:api-v1:edit-answerexercise",kwargs={"pk":answer_exercise.pk})
        api_client.force_authenticate(user=user_student)
        data = {
            "exercise":exercise,
            "student":user_student,
            "answer_text": "777777777777777"
        }
        response = api_client.put(url,data)
        print(response.data)
        response.status_code==200
