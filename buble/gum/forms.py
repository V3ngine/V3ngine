from django import forms


class LoginForm(forms.Form):
    name = forms.CharField(required=True)
    passwrd = forms.CharField(widget=forms.PasswordInput(), required=True)
    mail = forms.EmailField(required=True)
