from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUp, EditProfile, PasswordChanging


class ChangePassword(PasswordChangeView):
    form_class = PasswordChanging
    #form_class = PasswordChangeForm
    success_url=reverse_lazy("password_success")
    #success_url=reverse_lazy("edit_profile")

def password_success(request):
    return render(request, "registration/password_success.html", {})
class UserRegister(generic.CreateView):
    form_class=SignUp
    template_name="registration/register.html"
    success_url=reverse_lazy("login")

class UserEdit(generic.UpdateView):
    form_class=EditProfile
    template_name="registration/edit_profile.html"
    success_url=reverse_lazy("home")

    def get_object(self):
        return self.request.user

