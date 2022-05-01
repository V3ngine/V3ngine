from django.contrib import admin
from .models import Category, CreateUsers, CreatePost

# Register your models here.
admin.site.register(CreateUsers)
admin.site.register(CreatePost)
admin.site.register(Category)