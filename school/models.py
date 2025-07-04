from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class School(models.Model):
    name = models.CharField(max_length=150)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)


class Teacher_School(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)
    school = models.ForeignKey(School,on_delete=models.CASCADE)

class ClassRoom(models.Model):
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Lesson(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

class Studen_Lesson(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)



class News(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)