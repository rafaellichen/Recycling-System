from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout,authenticate, login
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from . import forms


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print (username, password)
        user = authenticate(username = username, password=password)
        print (user)
        if user is None: return HttpResponse("Invalid Login")
        if request.user.is_authenticated(): return redirect ('/')
        login(request, user)
        return redirect ('/')

    return render(request, 'users/login.djhtml')


@csrf_exempt
def signout(request):
    logout(request)
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        userForm = forms.SignupForm(request.POST or None)
        if ( userForm.is_valid()
             and userForm.cleaned_data['password'] ==
              userForm.cleaned_data['confirm_password']):
                user = userForm.save()
                user.set_password(user.password)
                user.save()
                return HttpResponse('signup succcessful\
                    <a href="/login"> login</a>')
        else:
            return HttpResponse('something wrong!')

    context = {
        'signupForm' : forms.SignupForm
    }
    return render(request, 'users/signup.djhtml', context=context)


def profile(request):
    return render(request, 'users/profile.djhtml')
