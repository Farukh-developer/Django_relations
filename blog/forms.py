from django import forms
from .models import Student, Category, Product


# creating forms here

class StudentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    age=forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"number"}))

    
    
    class Meta:
        model=Student
        fields=('name', 'age','teacher', 'group')   
        
######################


class Productfrom(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput({"class":"form-control"}))
    price=forms.CharField(widget=forms.TextInput({"class":"form-control", "type":"number"}))
    
    

    
    
    class Meta:
        model=Product
        fields=('name', 'description', 'price', 'category', 'image')                   
                                
class SearchForm(forms.Form):
    query=forms.CharField(label='Search', max_length=200)        