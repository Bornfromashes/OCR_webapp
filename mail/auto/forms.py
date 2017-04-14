from django import forms
from .models import student_info, history

class info(forms.ModelForm):
    name= forms.CharField(label= 'Enter name')
    reg_no= forms.CharField(label= 'Enter registration no.')
    email= forms.EmailField(label= 'Enter email')
    class Meta:
        model= student_info
        fields= ['name', 'reg_no', 'email',]
