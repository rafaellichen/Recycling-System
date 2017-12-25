# -*- coding: utf-8 -*-
'''Views for Recycle101'''
from django.shortcuts import render
from recycle101.models import HowTo
from django.http import HttpResponse
import json
# Create your views here.

def index(request):
    """
    This Method renders the main.html for route ('/recycle101') 
    
    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template recycle101/main.html being sent over 
    """
    return render(request, 'main.html')

def searchHowTo(request):
    """
    This Method renders the main.html for route ('/search101') 
    Searches for the HowTo based on the post request args

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template recycle101/main.html being sent over
        context: 'data' - result obtained from querying the request.POST['recycleType'] 
    """
    if request.method == 'POST':
        recycleType = request.POST['recycleType']
        # print (recycleType)
        result = list(HowTo.objects.filter(recycleType=recycleType).values())
        # print (result)
        return render(request, 'main.html', {"data": result})

def getItemTypes(request):
    """
    This Method sends of the HttpResponse of the query result
    Searches for the HowTo based on the post request args

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        HttpResponse object:
            data: String JSON with objects (id and value) for the JQuery UI to render
            application type : Json
    """
    # if the request that is being sent over is a ajax request
    if request.is_ajax():
        # get the keyword from the request
        keyword = request.GET.get('term')
        # query the database for any entity that is like the keyword but only get the top 10 results
        queryResult = list(HowTo.objects.filter(recycleType__icontains = keyword)[:10].values())
        # testing
        # print (queryResult)
        # need to return a json with the feilds (id and value)
        results = []
        for value in queryResult:
            value_json = {}
            value_json['id'] = value['id']
            value_json['value'] = value['recycleType']
            results.append(value_json)
        data = json.dumps(results)
    return HttpResponse(data, 'application/json')
