from django.contrib import admin

# Register your models here.
from .models import Category, Product, Teacher, Student, Group

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
