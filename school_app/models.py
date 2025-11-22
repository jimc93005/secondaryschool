from django.db import models
from django.contrib.auth.models import User


class Departments(models.Model):
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.text


class Subjects(models.Model):
    department_subjects = models.ForeignKey(Departments, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'subjects'

    def __str__(self):
        return self.text


class HoursperWeek(models.Model):
    hours_subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class SubjectTopics(models.Model):
    topics_subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='topics_subjects')
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class SubjectTeacher(models.Model):
    teacher_subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='teacher_subject')
    text = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text






# Create your models here.
