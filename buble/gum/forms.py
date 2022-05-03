
from django import forms

from .models import CreatePost, CreateUsers


class LoginForm(forms.ModelForm):

    class Meta:
        model = CreateUsers
        fields = ['name', 'password', 'mail']

        widgets = {

            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'mail' : forms.EmailInput(attrs={'class': 'form-control'}),


        }

        labels = {
            'password': 'Enter password',
            'name': 'Enter name',
            'mail': 'Enter email',
        }

    # name = forms.CharField(label='Имя пользователя', required=True)
    # password = forms.CharField(label='Пароль', widget=forms.PasswordInput(), required=True)
    # mail = forms.EmailField(label='Электронная почта', required=True)


class PostForm(forms.ModelForm):

    class Meta:
        model = CreatePost
        fields = ['title', 'message', ]

        widgets = {

            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'message' : forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 10,}),
            
        }

        labels = {

            'title': 'Enter your title',
            'message': 'Enter article',
            
        }


    # title = forms.CharField(label='Заголовок',max_length=100)
    # message = forms.CharField(label='Пост',max_length=1000, widget=forms.Textarea())
    # author = forms.CharField(label='Автор',max_length=30)
