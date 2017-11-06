from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout,authenticate, login
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# from . import forms


def signin(request):
    pass

@csrf_exempt
def signout(request):
    pass
def signup(request):
    pass

def profile(request):
    pass
