from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm

# Create your views here.

def index(request):
   return HttpResponse('Hello world')

def regform(request):
   if request.method == "POST":
      form = LoginForm(request.POST)
      if form.is_valid():
         print(form.cleaned_data)
   form = LoginForm()
   return render(request, 'regforms.html', {'form': form})
