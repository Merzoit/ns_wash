#IMPORT
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

#LOCAL IMPORT
from .forms import LoginUserForm

class LoginView(LoginView):
    """ Вход """
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('/q')
    def get_success_url(self):
        return self.success_url


class LogoutView(LogoutView):
    """ View for logout """
    pass


