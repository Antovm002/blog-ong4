from django import forms
from .models import Post

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields = ("titulo", "author", "contenido")

        widgets = {
            'titulo': forms.TextInput(attrs= {"class": "form-control", "placeholder"  : "Ingrese el Titulo..."}),
            'author': forms.Select(attrs= {"class": "form-control"}),
            'contenido': forms.Textarea(attrs= {"class": "form-control", "placeholder"  : "Ingrese el Texto..."})
        }