from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return f"{self.name}"

    
class Product(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField(default='', blank=True)
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    image=models.ImageField(upload_to='product_images', null=True)
   
     

    def __str__(self):
        return f"{self.name}"
    
#################################### Teacher , Student, Group.









class Group(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

class Teacher(models.Model):
    name=models.CharField(max_length=150)
    group=models.ForeignKey(Group, on_delete=models.CASCADE, related_name="teachers")    

    def __str__(self):
        return f"{self.name}"



class Student(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    teacher=models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="teacher")
    group=models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name}"
