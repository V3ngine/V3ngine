from django.db import models

# Create your models here.

class CreateUsers(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    password = models.CharField(unique=True, max_length=30)
    mail = models.EmailField(max_length=50)
