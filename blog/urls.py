from django.urls import path
from .views import category, product, group, teacher, student, create_student, update_student, delete_student, read_student

urlpatterns = [
    path('category',category, name="category_page" ),
    path('product/<int:id>/',product, name="product" ),
    
    
    path('group',group, name="group" ),
    path('teacher/<int:id>/',teacher, name="teacher" ),
    path('student/<int:id>/',student, name="student" ),
    
    
    path('create/',create_student, name='create_student'),
    path('read/<int:id>/',read_student, name="read_student" ),
    path('update/<int:id>/',update_student, name="update_student" ),
    path('delete/<int:id>/',delete_student, name="delete_student" ),
    
    
    
    
    
    
    
    
    
]
