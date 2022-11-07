from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class LoginView(LoginView):
    """ View for users auth """
    pass


class LogoutView(LogoutView):
    """ View for logout """
    pass


