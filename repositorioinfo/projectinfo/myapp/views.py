
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


#def home (request):
    #return render(request, "home.html", {})

class Home(ListView):
    model = Post
    template_name = "home.html"  
    #ordering = ["-id"] (ordena las publicaciones de mas reciente a menos reciente)

class Article(DetailView):
    model = Post
    template_name = "article.html"

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_section.html"
    #fields = ("titulo", "author", "contenido")

class Update(UpdateView):
    model = Post
    template_name = "update.html"
    fields = ["titulo", "contenido"]

class Delete(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")