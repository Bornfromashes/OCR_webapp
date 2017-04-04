from __future__ import unicode_literals

from django.db import models

# Create your models here.
class student_info(models.Model):
    name=models.CharField(max_length=40, help_text="Enter Name")
    reg_no=models.IntegerField(help_text='Enter your reg_no', primary_key=True)
    reg_no=models.ForeignKey('reg_no', on_delete=models.CASCADE)
    email=models.EmailField(help_text='Enter email')
    def __str__(self):
        return self.name

class History(models.Model):
    reg_no=models.ForeignKey('reg_no', on_delete=models.CASCADE)
    reg_no=models.IntegerField(primary_key=True)
    date=models.DateTimeField(auto_now=True)

class Admin(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
