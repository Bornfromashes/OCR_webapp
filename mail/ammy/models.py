from django.db import models
class Student_info(models.Model):
	Name = models.CharField(max_length=50)
	mail = models.CharField(max_length=50)
	Reg_no = models.IntegerField()
	class Meta:
		db_table = "Student_info"
