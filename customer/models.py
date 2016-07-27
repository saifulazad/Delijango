from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    email_address = models.EmailField()
    password = models.CharField(max_length=20)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)