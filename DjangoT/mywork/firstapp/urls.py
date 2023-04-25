from django.urls import path  
from . import views    

urlpatterns =[
    path('', views.index , name='index'),
    path('counter', views.counter, name='counter'),
    path('onepage', views.onepage, name='onepage'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
   
    



]