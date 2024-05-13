from django import forms
from .models import Student


# creating forms here

class StudentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    age=forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"number"}))

    
    
    class Meta:
        model=Student
        fields=('name', 'age','teacher', 'group')                   
        