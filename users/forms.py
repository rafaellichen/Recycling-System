'''Forms currently creates SignupForm object'''
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):
    '''Class SignupForm that takes forms.ModelForm as input param'''
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
