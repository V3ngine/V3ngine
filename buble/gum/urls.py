from django import views
from django.urls import path

from . import views

app_name = 'gum'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('regform/', views.regform, name='regform'),
    path('base/', views.base, name='base'),
    path('all_posts', views.all_posts, name='all_posts'),
    
    
]