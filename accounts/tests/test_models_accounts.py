import pytest
from accounts.models import User

@pytest.mark.django_db
def test_User_model():
    instance = User.objects.create(username='Test Name')
    assert instance.username == 'Test Name'
