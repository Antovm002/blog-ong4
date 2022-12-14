from django import forms
from .models import Post, Category, Comment
from django import forms
from django.db.models import fields


choices = Category.objects.all().values_list("name", "name")

choice_list = []

for item in choices:
    choice_list.append(item)
class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "author", "categoria", "contenido", "header_image")

        widgets = {
            'titulo': forms.TextInput(attrs= {"class": "form-control", "placeholder": "Ingrese el Título..."}),
            'author': forms.TextInput(attrs= {"class": "form-control", "value": "", "id": "admin", "type": "hidden"}),
            #'author': forms.Select(attrs= {"class": "form-control"}),
            'categoria': forms.Select(choices= choice_list, attrs= {"class": "form-control"}),
            'contenido': forms.Textarea(attrs= {"class": "form-control", "placeholder"  : "Ingrese el Texto..."})
        }


class EditForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "categoria", "contenido")

        widgets = {
            'titulo': forms.TextInput(attrs= {"class": "form-control", "placeholder": "Ingrese el Título..."}),
            'author': forms.TextInput(attrs= {"class": "form-control", "value": "", "id": "admin", "type": "hidden"}),
            #'author': forms.Select(attrs= {"class": "form-control"}),
            'categoria': forms.Select(choices= choice_list, attrs= {"class": "form-control"}),
            'contenido': forms.Textarea(attrs= {"class": "form-control", "placeholder"  : "Ingrese el Texto..."})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "contenido")
        widgets = {
            'name': forms.TextInput(attrs= {"class": "form-control", "placeholder": "Ingrese su nombre..."}),
            'contenido': forms.Textarea(attrs= {"class": "form-control", "placeholder"  : "Ingrese el texto..."})
        }