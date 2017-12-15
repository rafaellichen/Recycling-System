'''Views for Users App'''
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from . import forms
from mainRecycleApp.models import Bookmark, recyclinRecyclingCenter

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

@login_required
def profile(request):
    '''Profile render method that renders the Users/Profile and redirects if the user is not authenticated'''
    user = request.user
    if request.method == 'GET':
        bookmarks = getBookmrks(user)
        data = getFacilities(bookmarks)
        return render(request, 'users/profile.djhtml', {"data":data})
    else:
        pass

def index(request):
    '''Index render method that renders app/index'''
    return render(request, 'app/index.djhtml')


def getBookmarks(user):
    ''' Returns user's bookmarked recycling centers'''
    user_bookmarks = Bookmark.objects.filter(
                        user=request.user).values_list('idc')
    return list(set(user_bookmarks))

def getFacilities(idc_list):
    '''Queries db for recycling center and groups the data in a context dict'''
    result = list(RecyclingCenter.objects.filter(idc__in=idc_list).values())
    final = {}
    for cur_element in result:
        keys = (cur_element["idc"])
        if keys in final:  # combine when have same "idc"
            final[keys] = {"name": cur_element["name"], "address": cur_element["address"], "Monday": cur_element["Monday"], "Tuesday": cur_element["Tuesday"], "Wednesday": cur_element["Wednesday"], "Thursday": cur_element["Thursday"], "Friday": cur_element["Friday"], "Saturday": cur_element["Saturday"], "Sunday": cur_element["Sunday"], "borough": cur_element["borough"], "zip": cur_element["zip"],  "cell": cur_element["cell"], "picksup": cur_element["picksup"], "cell":cur_element["cell"], "url": cur_element["url"], "type": cur_element["type"] + "," +final[keys]["type"]}
        else:  # for unique "idc"
            final[keys] = {"name": cur_element["name"], "address": cur_element["address"], "Monday": cur_element["Monday"], "Tuesday": cur_element["Tuesday"], "Wednesday": cur_element["Wednesday"], "Thursday": cur_element["Thursday"], "Friday": cur_element["Friday"], "Saturday": cur_element["Saturday"], "Sunday": cur_element["Sunday"], "borough": cur_element["borough"], "zip": cur_element["zip"],  "cell": cur_element["cell"], "picksup": cur_element["picksup"], "cell":cur_element["cell"], "url": cur_element["url"], "type": cur_element["type"]}
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
