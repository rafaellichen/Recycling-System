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
        # print (recycleType)
        result = list(HowTo.objects.filter(recycleType=recycleType).values())
        # print (result)
        return render(request, 'main.html', {"data": result})

def getItemTypes(request):
    # if the request that is being sent over is a ajax request
    if request.is_ajax():
        # get the keyword from the request
        keyword = request.GET.get('term')
        # query the database for any entity that is like the keyword
        queryResult = HowTo.objects.filter(recycleType__icontains = keyword)
        print (queryResult)
