from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class School(models.Model):
    name = models.CharField(max_length=150)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"

class Teacher_School(models.Model):
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={"role":"teacher"})
    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher.name}"

class ClassRoom(models.Model):
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={"role":"teacher"})
    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class ClassRoom_Student(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={"role":"student"})
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)


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
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={"role__in":["teacher","admin"]})
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class Exercise(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    deadline = models.DateTimeField()
    file = models.FileField(upload_to="exercise_files/",blank=True,null=True)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    classroom = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={"role__in":["teacher","admin"]})
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}-{self.title}"

class AnswerExercise(models.Model):
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    answer_text = models.TextField()
    answer_file = models.FileField(upload_to="answer_exercise/",blank=True,null=True)
    submited_date = models.DateTimeField(auto_now_add=True)

