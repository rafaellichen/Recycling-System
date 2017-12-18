# -*- coding: utf-8 -*-
'''Views for Recycle101'''
from django.shortcuts import render
from recycle101.models import HowTo

# Create your views here.
def index(request):
    '''Index render method for recycle101'''
    return render(request, 'main.html')

def searchHowTo(request):
    if request.method == 'POST':
        recycleType = request.POST['recycleType']
        print (recycleType)
        result = list(HowTo.objects.filter(recycleType=recycleType).values())
        print (result)
        return render(request, 'main.html', {"data": result})
        