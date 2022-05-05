
from django.views.generic import DetailView, UpdateView, DeleteView,ListView
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LoginForm
from .models import Category, CreatePost
from .forms import PostForm


# Create your views here.

def index(request):
    return HttpResponse('Hello world')


def regform(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('gum:home')
    form = LoginForm()
    return render(request, 'regforms.html', {'form': form})


def base(request):
    return render(request, 'base.html') 


def crud_form(request):
    if request.method == "POST":
        form_post = PostForm(request.POST)
        if form_post.is_valid():
            create_post = CreatePost()
            create_post.title = form_post.cleaned_data['title']
            create_post.message = form_post.cleaned_data['message']
            # create_post.author = form_post.cleaned_data['author']
            create_post.save()
            print(form_post.cleaned_data)
            return redirect('gum:all_posts')
    form_post = PostForm()

    data = {
        'form': form_post
    }
   
    return render(request, 'crud_form.html',  data)


class PostView(ListView):
    paginate_by = 4
    model = CreatePost
    template_name = 'all_posts.html'
    context_object_name = 'all_posts'


class DetailPost(DetailView):
    model = CreatePost
    template_name = 'detail.html'
    context_object_name = 'post'
    

class UpDate(UpdateView):
    model = CreatePost
    form_class = PostForm
    template_name = 'solution.html'
   

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('gum:home')


class DeletePost(DeleteView):
    model = CreatePost
    template_name = 'delete_post.html'
    fields = ['title', 'message']
    success_url = '/all_posts/'


class HomeView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'all_posts'
    queryset = Category.objects.all()[2:]


class ShowProdacts(ListView):
    model = Category
    template_name = 'all_posts.html'
    context_object_name = 'all_posts'
   
    def get_queryset(self):
        group =  CreatePost.objects.filter(category_id=self.kwargs['category_id'])
        return group



# def all_posts(request):

#     pub_posts = CreatePost.objects.all()

#     return render(request, 'all_posts.html', {'all_posts':pub_posts})


# def detail_post(request, str):
#     detail = CreatePost.objects.all().filter(id=str)

#     data = {
#         'post': detail
#     }
#     return render(request, 'detail.html', data )
