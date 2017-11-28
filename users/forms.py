'''Forms currently creates SignupForm object'''
from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):
    '''Class SignupForm that takes forms.ModelForm as input param'''
    username = forms.CharField(label=(u'User Name'))
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def clean_username(self):
    	'''Check if username already exists in the database or not'''
    	user = User.objects.filter(username__iexact = self.cleaned_data['username'])
    	if not user:
    		return self.cleaned_data['username']
    	else:
    		raise forms.ValidationError('Your username already exists')

    def clean_email(self):
    	'''Check if email already exists in the database or not'''
    	user = User.objects.filter(username__iexact = self.cleaned_data['email'])
    	if not user:
    		return self.cleaned_data['email']
    	else:
    		raise forms.ValidationError('Your email already exists')

    def clean(self):
    	'''Check if the password and the password confirmation matches or not'''
    	if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
    		raise forms.ValidationError('Your passwords does not match.')
    	else:
    		return self.cleaned_data['confirm_password']
