from django.db import models
from django.urls import reverse



# Create your models here.


class CreateUsers(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    password = models.CharField( max_length=255, verbose_name='Пароль')
    mail = models.EmailField( max_length=255, verbose_name='Почта')
    pub_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'title : {self.name} , id : {self.id}'


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')
    image = models.ImageField(upload_to='category', null=True, verbose_name='Фото')
    
    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return f'title : {self.name} , id : {self.id}'

    def get_absolute_url(self):
        return reverse('gum:category', kwargs={'category_id': self.pk})
    

class CreatePost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    image = models.ImageField(upload_to='post_img',blank=True, verbose_name='Фото')
    message = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    author = models.CharField(max_length=30, verbose_name='Авторы')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']

    def __str__(self) -> str:
        return f'Статья : {self.title} id : {self.id}'

    
    def get_absolute_url(self):
        return reverse('gum:detail', kwargs={'pk': self.id})
    
    

