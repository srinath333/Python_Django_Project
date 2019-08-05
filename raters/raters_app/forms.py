from django import forms
from raters_app.models import *
class signUp(forms.Form):

        ID= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))


        age=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        gender= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))
        Workflow=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))


class Login(forms.Form):
    ID = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter'}))