from django.shortcuts import render
def crudops(request):

	#Creating an entry

	Student_info=Student_info(Name=Amit, mail=amit220698@gmail.com,Reg_no=16408)
	dreamreal.save()

	#Read ALL entries
	objects = Student_info.objects.all()
	res ='Printing all Student_info entries in the DB : <br>'
	for elt in objects:
		res+=elt.name+"<br>"
