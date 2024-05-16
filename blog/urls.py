from django.urls import path
from .views import home, category, information, read, create_home, update_home, delete_home, search_product

urlpatterns = [
   
   
    path('home',home, name="home"),
    path('category/<int:id>/',category, name='category'),
    path('information/<int:id>/',information, name='information'),
    
    
    path('create_home/',create_home, name='create_home'),
    path('read/<int:id>/',read, name='read_home'),
    path('update/<int:id>/',update_home, name='update_home'),
    path('delete/<int:id>/',delete_home, name='delete_home'),
    
    path('search/',search_product, name='search_product')
    
    

    
    
    
]
