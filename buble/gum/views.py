from django.http import HttpResponse
from django.shortcuts import render
from .forms import LoginForm
from .models import CreatePost


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

def base(request):
    return render(request, 'base.html') 

def all_posts(request):
    pub_posts = CreatePost.objects.all()

    return render(request, 'all_posts.html', {'all_posts':pub_posts})