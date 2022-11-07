#IMPORT
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

#LOCAL IMPORT



class LoginUserForm(AuthenticationForm, forms.ModelForm):
    """ LogIn form """
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Charfield
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
