import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def admin_user():
    user = User.objects.create_user(username="test",password="123",is_staff=True,role="admin")
    return user 

@pytest.fixture
def student_user():
    student = User.objects.create_user(username="4445552211",password="123",role="student")
    return student

@pytest.fixture
def teacher_user():
    teacher = User.objects.create_user(username="teach",password="123",role="teacher")
    return teacher


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
class TestGetApi:
    def test_get_users(self,admin_user,api_client):
        client = api_client
        url = reverse("accounts:api-v1:get-users")
        client.force_authenticate(user=admin_user)
        respone = client.get(url)
        assert respone.status_code == 200


@pytest.mark.django_db
class TestPostApi:
    def test_post_register_teacher(self, api_client):
        url = reverse("accounts:api-v1:user-register", kwargs={"role": "teacher"})
        data = {
            "name": "test",
            "family": "test",
            "codemeli": "7778889674",
            "username": "tecah",
            "password": "123",
            "password_confirm": "123",
            "role": "teacher"
        }
        response = api_client.post(url, data, format="json")
        print(response.data)
        assert response.status_code == 200

    def test_post_register_student(self,api_client):
        url = reverse("accounts:api-v1:user-register", kwargs={"role": "student"})
        data = {
            "name" : "test",
            "family":"test",
            "username":"stu",
            "codemeli":"4561233652",
            "password" :"123",
            "password_confirm":"123",
            "role":"student" 
        }
        response = api_client.post(url,data)
        assert response.status_code==200
    
    def test_login_teacher(self,api_client,teacher_user):
        url = reverse("accounts:api-v1:user-login",kwargs={"role":"teacher"})
        data ={
            "username":"teach",
            "password":"123"
        }
        response = api_client.post(url,data)
        assert "access" in response.data
        assert response.status_code==200
    
    def test_login_student(self,api_client,student_user):
        url = reverse("accounts:api-v1:user-login",kwargs={"role":"student"})
        data ={
            "codemeli":"4445552211",
            "password":"123"
        }
        response = api_client.post(url,data)
        assert "access" in response.data
        assert response.status_code ==200