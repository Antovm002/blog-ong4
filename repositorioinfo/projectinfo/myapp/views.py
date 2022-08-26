from urllib import request
from django.shortcuts import render, get_object_or_404
from django.template import ContextPopException
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


#def home (request):
    #return render(request, "home.html", {})

def Info(request):
    return render(request, "info.html")

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get("post_id"))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse("article-detail", args=[str(pk)]))

class Home(ListView):
    model = Post
    template_name = "home.html" 
    ordering = ["-post_date"] 
    #ordering = ["-id"] 
    #(ordena las publicaciones de mas reciente a menos reciente)

    def get_context_data(self, *atgs, **kwargs):
        categoria_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*atgs, **kwargs)
        context["categoria_menu"] = categoria_menu
        return context

def CategoryList (request):
    categoria_lista_menu = Category.objects.all()
    return render(request, "category_list.html", {"categoria_lista_menu": categoria_lista_menu})

def Categorys (request, categoria):
    category_posts = Post.objects.filter(categoria=categoria.replace("-", " "))
    return render(request, "categorys.html", {"categoria": categoria.replace("-", " "), "category_posts": category_posts})

class Article(DetailView):
    model = Post
    template_name = "article.html"
    
    def get_context_data(self, *args, **kwargs):
        categoria_menu = Category.objects.all()
        context = super(Article, self).get_context_data(*args, **kwargs)

        algo = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes=algo.total_likes()

        liked = False
        if algo.likes.filter(id=self.request.user.id).exists():
            liked=True
        context["categoria_menu"] = categoria_menu
        context["total_likes"]= total_likes
        context["liked"]=liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_section.html"
    def get_context_data(self, *atgs, **kwargs):
        categoria_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*atgs, **kwargs)
        context["categoria_menu"] = categoria_menu
        return context
    #fields = ("titulo", "author", "contenido")

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    #fields = "__all__"
    success_url = reverse_lazy("home")

class AddCategory(CreateView):
    model = Category
    #form_class = PostForm
    fields = "__all__"
    template_name = "add_category.html"
    def get_context_data(self, *atgs, **kwargs):
        categoria_menu = Category.objects.all()
        context = super(AddCategory, self).get_context_data(*atgs, **kwargs)
        context["categoria_menu"] = categoria_menu
        return context

class Update(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update.html"

class Delete(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")