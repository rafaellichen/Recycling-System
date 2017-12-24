'''Views for Users App'''
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import forms
from collections import OrderedDict
from mainRecycleApp.models import Bookmark, RecyclingCenter
from django.http import JsonResponse
import json

def signin(request):
    '''Signin method with param request'''
    args = {}
    if request.method == 'POST':
        LOGINFORM = forms.LoginForm(request.POST or None)
        if LOGINFORM.is_valid():
            user = authenticate(username=LOGINFORM.cleaned_data('username'), password=LOGINFORM.cleaned_data('username'))
            print (user)
            if request.user.is_authenticated(): return redirect('/')
            login(request, user)
    else:
        LOGINFORM = forms.LoginForm()
    args['form'] = LOGINFORM
    print (args)
    return render(request, 'users/login.djhtml', args)

def editProfile(request):
    return render(request, 'users/login.djhtml')

@csrf_exempt
def signout(request):
    '''Signout Method with param request'''
    logout(request)
    return redirect('/')

def signup(request):
    '''Signup Method with param request'''
    args = {}
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
    args['form'] = USERFORM
    return render(request, 'users/signup.djhtml', args)

@login_required
def profile(request):
    '''Profile render method that renders the Users/Profile and redirects if the user is not authenticated'''
    user = request.user
    if request.method == 'GET':
        bookmarks = getBookmarks(user)
        data = getFacilities(bookmarks)
        # print(data)
        return render(request, 'users/profile.djhtml', {"data":data})
    else:
        pass

@login_required
def editProfile(request):
    '''Users to edit the profile'''
    args = {}
    if request.method == 'POST':
        EDITFORM = forms.EditProfile(request.POST or None)
        if EDITFORM.is_valid():
            EDITFORM.save()
            user_first_name = EDITFORM.cleaned_data['first_name']
            return render(request, 'users/profile.djhtml', {'user': user_first_name})
    else:
        EDITFORM = forms.EditProfile()
    args['form'] = EDITFORM
    return render(request, 'users/editProfile', args)


def index(request):
    '''Index render method that renders app/index'''
    return render(request, 'app/index.djhtml')


def getBookmarks(user):
    ''' Returns user's bookmarked recycling centers'''
    user_bookmarks = user.bookmarks.all().values_list('facility', flat=True)
    return list(set(user_bookmarks))

def getFacilities(idc_list):
    '''Queries db for recycling center and groups the data in a context dict'''
    result = list(RecyclingCenter.objects.filter(idc__in=idc_list).values())
    final = {}
    for cur_element in result:
        keys = (cur_element["idc"])
        if keys in final:  # combine when have same "idc"
            final[keys] = {"idc": cur_element['idc'],"name": cur_element["name"], "address": cur_element["address"], "Monday": cur_element["Monday"], "Tuesday": cur_element["Tuesday"], "Wednesday": cur_element["Wednesday"], "Thursday": cur_element["Thursday"], "Friday": cur_element["Friday"], "Saturday": cur_element["Saturday"], "Sunday": cur_element["Sunday"], "borough": cur_element["borough"], "zip": cur_element["zip"],  "cell": cur_element["cell"], "picksup": cur_element["picksup"], "url": cur_element["url"], "type": cur_element["type"] + "," +final[keys]["type"]}
        else:  # for unique "idc"
            final[keys] = {"idc": cur_element['idc'],"name": cur_element["name"], "address": cur_element["address"], "Monday": cur_element["Monday"], "Tuesday": cur_element["Tuesday"], "Wednesday": cur_element["Wednesday"], "Thursday": cur_element["Thursday"], "Friday": cur_element["Friday"], "Saturday": cur_element["Saturday"], "Sunday": cur_element["Sunday"], "borough": cur_element["borough"], "zip": cur_element["zip"],  "cell": cur_element["cell"], "picksup": cur_element["picksup"], "url": cur_element["url"], "type": cur_element["type"]}
    for i in final:
        final[i]["type"]=final[i]['type'].split(",")
        if(final[i]["Monday"]!="closed"):
            temp = final[i]["Monday"].split(",")
            final[i]['Monday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        if(final[i]["Tuesday"]!="closed"):
            temp = final[i]["Tuesday"].split(",")
            final[i]['Tuesday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        if(final[i]["Wednesday"]!="closed"):
            temp = final[i]["Wednesday"].split(",")
            final[i]['Wednesday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        if(final[i]["Thursday"]!="closed"):
            temp = final[i]["Thursday"].split(",")
            final[i]['Thursday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        if(final[i]["Friday"]!="closed"):
            temp = final[i]["Friday"].split(",")
            final[i]['Friday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        if(final[i]["Saturday"]!="closed"):
            temp = final[i]["Saturday"].split(",")
            final[i]['Saturday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        if(final[i]["Sunday"]!="closed"):
            temp = final[i]["Sunday"].split(",")
            final[i]['Sunday']=temp[0][0:2]+":"+temp[0][2:]+"  -"+temp[1][0:2]+":"+temp[1][2:]
        final[i]["len"]=len(final[i]["type"])
    final = OrderedDict(sorted(final.items(), key=lambda kv: kv[1]['len'], reverse=True))
    returnval = []
    for i in final:
        returnval.append(final[i])
    return returnval

def bookmarkHandler(request):
    '''Adds/removes facility to user bookmarks'''
    body = json.loads(request.body.decode("utf-8"))
    idc = body['idc']
    param = body['param']
    if param == 'add':
        newBookmark = Bookmark(facility=idc, user=request.user)
        newBookmark.save()
    elif param =='remove':
        Bookmark.objects.filter(facility=idc, user=request.user).delete()
    return JsonResponse({'result':'success'})
