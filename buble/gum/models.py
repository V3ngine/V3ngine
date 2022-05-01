from django.db import models


# Create your models here.


class CreateUsers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( unique=True, max_length=50)
    password = models.CharField( max_length=30)
    mail = models.EmailField( max_length=50)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return f'title : {self.name} , id : {self.id}'


class Category(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    image = models.ImageField(upload_to='category', null=True)
    
    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return f'title : {self.name} , id : {self.id}'

    # def get_absolute_url(self):
    #     return reverse('category', kwargs={'category_id': self.pk})
    

class CreatePost(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_img',blank=True)
    message = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['id']

    def __str__(self) -> str:
        return f'title : {self.title} id : {self.id}'

    
    def get_absolute_url(self):
        return  f'/all_posts'

    
    

