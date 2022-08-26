from django.contrib import admin
from .models import Post, Category, Comment
from django.contrib import admin
from .models import CrispyModel

admin.site.register(CrispyModel)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)