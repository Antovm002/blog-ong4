from django.urls import path
from .views import UserRegister, UserEdit, ChangePassword
#from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
    path("edit_profile/", UserEdit.as_view(), name="edit_profile"),
    #path("password/", auth_views.PasswordChangeView.as_view(template_name="registration/change_password.html")),
    path("password/", ChangePassword.as_view(template_name="registration/change_password.html")),
    path("password_success/", views.password_success, name="password_success"),
    

]