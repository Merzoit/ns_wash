#IMPORT
from django.urls import path, include

#LOCAL IMPORT
from .views import *

urlpatterns = [
    path('', LoginView.as_view())
]