from django.db import models
from django.contrib.auth.models import User # 3-7

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #3-7
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    #subject = models.ForeignKey(Question, on_delete=models.CASCADE)  # 3-7 이전
    author = models.ForeignKey(User, on_delete=models.CASCADE) #3-7
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

# Create your models here.
