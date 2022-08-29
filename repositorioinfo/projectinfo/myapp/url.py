from django.urls import path
from .views import Home, Article, AddPost, Update, Delete, AddCategory, Categorys, CategoryList, LikeView, AddComment, Info

urlpatterns = [
   # path('', views.home, name = "home"),
   path('', Home.as_view(), name="home"),
   path('article/<int:pk>', Article.as_view(), name="article-detail"),
   path('post_section/', AddPost.as_view(), name = "add_post"),
   path('add_category/', AddCategory.as_view(), name = "add_category"),
   path('article/edit/<int:pk>', Update.as_view(), name="update"),
   path('article/<int:pk>/remove', Delete.as_view(), name="delete"),
   path('category/<str:categoria>/', Categorys, name="add_category"),
   path('category_list/', CategoryList, name="category_list"),
   path('like/<int:pk>', LikeView, name="like_post"),
   path('article/<int:pk>/comment/', AddComment.as_view(), name="add_comment"),
   path('info/', Info, name="info"),
]