from django.db import models

# Create your models here.


class CreateUsers(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField( unique=True, max_length=50)
    password = models.CharField( max_length=30)
    mail = models.EmailField( max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'title : {self.name} uid : {self.uid}'


class CreatePost(models.Model):
    uid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return f'title : {self.title} uid : {self.uid}'
