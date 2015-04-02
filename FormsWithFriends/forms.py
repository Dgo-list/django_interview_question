from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Style', 'autocomplete':'off'}),
            "first_name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'John', 'autocomplete':'off'}),
            "last_name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Smith', 'autocomplete':'off'}),
            "email":forms.TextInput(attrs={'class':'form-control', 'placeholder':'thedoctor@test.co.uk', 'autocomplete':'off'}),
            "password":forms.TextInput(attrs={'class':'form-control', 'type':'password', 'autocomplete':'off'}),
          }