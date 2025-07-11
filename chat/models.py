from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Chatroom(models.Model):
    name = models.CharField(max_length=150)
    members = models.ManyToManyField(User)
    
    def __str__(self):
        return f"{self.name}"

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    chatroom = models.ForeignKey(Chatroom,on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now_add=True)
