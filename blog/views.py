from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Teacher, Student, Group
from .forms import StudentForm, Productfrom
# Create your views here.
from .models import Category, Product

def home(request):
    products=Product.objects.all()
    categories=Category.objects.all()
    return render(request, 'home.html', context={"products":products, "categories":categories})

def read(request, id):
    product=Product.objects.get(id=id)
    return render(request, 'read_home.html', context={"product":product})


def create_home(request):
    form=Productfrom()
    
    if request.method=='POST':
        form=Productfrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'create_home.html', context={"form":form})


def update_home(request, id):
    product=get_object_or_404(Product, id=id)
    form=Productfrom(instance=product)
    if request.method=='POST':
        form=Productfrom(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/home')
    return render(request, 'create_home.html', context={"form":form})


def delete_home(request, id):
    product=get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/home')


    


    
def category(request, id):
    category=get_object_or_404(Category, id=id)
    products=category.products.all()
    categories=Category.objects.all()
    return render(request, 'home.html', context={"products":products, "categories":categories})

def information(request, id):
    product=get_object_or_404(Product, id=id)
    categories=Category.objects.all()
    return render(request, 'information.html', context={"product":product, "categories":categories})
################################################







