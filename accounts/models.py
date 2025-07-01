from django.db import models

class User(models.Model):
    Roel_User =[
        ('admin','Admin'),
        ('teacher','Teacher'),
        ('student','Student'),
    ]
    
    name = models.CharField(max_length=150)
    family = models.CharField(max_length=150)
    codemeli = models.BigIntegerField()
    username = models.CharField(max_length=150, unique=True)  
    password = models.CharField(max_length=150)
    role = models.CharField(max_length=10, choices=Roel_User)
    confirmation = models.BooleanField(default=False)  
    biography = models.TextField(blank=True, null=True) 
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)  
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
