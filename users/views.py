'''Views for Users App'''
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from . import forms

def signin(request):
    '''Signin method with param request'''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print (username, password)
        user = authenticate(username=username, password=password)
        # print (user)
        if user is None: return HttpResponse("Invalid Login")
        if request.user.is_authenticated(): return redirect('/')
        login(request, user)
        return redirect('/')
    return render(request, 'users/login.djhtml')


@csrf_exempt
def signout(request):
    '''Signout Method with param request'''
    logout(request)
    return redirect('/')

def signup(request):
    '''Signup Method with param request'''
    if request.method == 'POST':
        USERFORM = forms.SignupForm(request.POST or None)
        if USERFORM.is_valid():
            user = USERFORM.save(commit=False)
            user.set_password(USERFORM.cleaned_data['password'])
            user.save()
            user_first_name = USERFORM.cleaned_data['first_name']
            return render(request, 'users/redirect.djhtml', {'user': user_first_name})
    else:
        USERFORM = forms.SignupForm()
    return render(request, 'users/signup.djhtml', {'signupForm' : USERFORM})


def profile(request):
    '''Profile render method that renders the Users/Profile and redirects if the user is not authenticated'''
    user = request.user
    if user.is_authenticated():
        return render(request, 'users/profile.djhtml')
    else:
        return redirect('/')


def index(request):
    '''Index render method that renders app/index'''
    return render(request, 'app/index.djhtml')
