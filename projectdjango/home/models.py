from django.db import models
from django.shortcuts import render
# Create your models here.


# class Question(models.Model):
#     text = models.CharField(max_length=200)
#     time_pub = models.DateTimeField()

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text= models.CharField(max_length=100)
#     vote = models.IntegerField(default=0)