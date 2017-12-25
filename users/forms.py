'''Forms currently creates SignupForm object'''
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django import forms

class SignupForm(forms.ModelForm):
    '''Class SignupForm that takes forms.ModelForm as input param'''
    password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Password'
        }))
    confirm_password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Confirm password'
        }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
        }

    def clean_username(self):
        '''Check if username already exists in the database or not'''
        user = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if not user:
            return self.cleaned_data['username']
        else:
            raise forms.ValidationError('Your username already exists')

    def clean_email(self):
        '''Check if email already exists in the database or not'''
        user = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if not user:
            return self.cleaned_data['email']
        else:
            raise forms.ValidationError('Your email already exists')


class LoginForm(forms.Form):
    '''Class LoginForm that takes forms.ModelForm as input param'''
    username = forms.CharField(widget=forms.TextInput({
        'placeholder': 'Username',
        'id' : 'username',
        'class' : 'form-control',
        }))
    password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Password',
        'id' : 'password',
        'class' : 'form-control',
        }))

    class Meta:
        fields = ['user_name', 'password']
        widgets = {
            'user_name': forms.TextInput(attrs={'placeholder': 'Username'}),
        }

    def clean(self):
        '''Check if the username or the password is valid or not and return validation error'''
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Your username or password is invalid')
        else:
            return self.cleaned_data

class EditProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'id': 'fName', 'class' : 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'id': 'LName', 'class' : 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email', 'id': 'email', 'class' : 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'id': 'username', 'class' : 'form-control'}),
        }

    def clean_username(self):
        '''Check if username already exists in the database or not'''
        user = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if not user:
            return self.cleaned_data['username']
        else:
            raise forms.ValidationError('Your username already exists')

    def clean_email(self):
        '''Check if email already exists in the database or not'''
        user = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if not user:
            return self.cleaned_data['email']
        else:
            raise forms.ValidationError('Your email already exists')
