from __future__ import unicode_literals

# Create your models here.

from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    email_address = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)