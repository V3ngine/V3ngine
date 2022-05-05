from django.contrib import admin

from .models import Category, CreateUsers, CreatePost

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'pub_date')
    search_fields = ('title',)
    list_filter = ('pub_date', )
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'pub_date' )
    search_fields = ('id',)


admin.site.register(CreateUsers, UsersAdmin)
admin.site.register(CreatePost, PostAdmin)
admin.site.register(Category, CategoryAdmin)


admin.site.site_title = 'Админ панель Boar'
admin.site.site_header = 'Админ панель Boar'


