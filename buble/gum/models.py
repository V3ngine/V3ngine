from json.encoder import INFINITY
from django.db import models

# Create your models here.

class CreateUsers(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    password = models.CharField(unique=True, max_length=30)
    mail = models.EmailField(max_length=50)

class CreatePost(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    pab_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
