from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Teacher, Student, Group
from .forms import StudentForm
# Create your views here.
def category(request):
    category=Category.objects.all()
    return render(request, 'category/category.html', context={"category":category})


def product(request, id):
    category=get_object_or_404(Category, id=id)
    products=category.products.all()
    return render(request, 'category/product.html', context={"products":products})
    
    
######################################################### Teacher, Student, Group

def group(request):
    group=Group.objects.all()
    return render(request, 'category/group.html', context={"group":group})


def teacher(request, id):
    group=get_object_or_404(Group, id=id)
    teacher=group.teachers.all()
    return render(request, 'category/teacher.html', context={"teacher":teacher})


def student(request, id):
    teacher=Teacher.objects.get(id=id) 
    students=teacher.teacher.all()
    return render(request, 'category/student.html', context={"students":students})

def read_student(request, id):
    students=Student.objects.get(id=id)
    return render(request, 'category/read_student.html', context={"students":students})

def create_student(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/group')
    return render(request, 'category/create_student.html', context={"form":form})
    
    
def update_student(request, id):
    students=Student.objects.get(id=id)
    form=StudentForm(instance=students)
    if request.method=='POST':
        form=StudentForm(request.POST, instance=students)
        if form.is_valid():
            form.save()
          
            return redirect('/group')
    
    return render(request, 'category/create_student.html', context={"form":form})

        

def delete_student(request, id):
    students=get_object_or_404(Student, id=id)
    students.delete()
    return redirect('/group')    
    
    

        