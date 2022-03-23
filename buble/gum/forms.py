from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    mail = forms.EmailField(required=True)

class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    message = forms.TextField(max_length=1000)
    author = forms.CharField(max_length=30)