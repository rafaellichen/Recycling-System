# -*- coding: utf-8 -*-
'''Views for Recycle101'''
from django.shortcuts import render
from recycle101.models import HowTo

# Create your views here.
def index(request):
    '''Index render method for mainrecycleApp/home'''
    return render(request, 'main.html')