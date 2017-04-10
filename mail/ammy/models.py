from __future__ import unicode_literals

from django.db import models

# Create your models here.
class student_info(models.Model):
    name=models.CharField(max_length=40, help_text="Enter Name")
    reg_no=models.IntegerField(help_text='Enter your reg_no', primary_key=True)
    email=models.EmailField(help_text='Enter email')
    def __str__(self):
        return self.name

class History(models.Model):

    Reg_no=models.ForeignKey('student_info', on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

class Admin(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
