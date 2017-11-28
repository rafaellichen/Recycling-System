# -*- coding: utf-8 -*-
'''Views for mainRecycleApp'''
from __future__ import unicode_literals

from mainRecycleApp.models import RecyclingCenter
from django.shortcuts import render
import sqlite3
import pandas as pd

# Create your views here.
def index(request):
    '''Index render method for mainrecycleApp/home'''
    return render(request, 'mainRecycleApp/home.html')

def about(request):
    '''About render method for mainRecycleApp/about.html'''
    return render(request, 'mainRecycleApp/about.html')

def contact(request):
    '''Contact render method for mainRecycleApp/contact.html'''
    return render(request, 'mainRecycleApp/contact.html')

def search_withQuery(request):
    '''Method to search with query from the database'''
    if request.method == 'GET':
        # category = request.GET.getlist("gtype")
        # day=request.GET.getlist("day")
        # time = request.GET.getlist("dropdown")[0]
        # zipcode = request.GET.getlist("zipcode")[0]
        # result = RecyclingCenter.objects.all().order_by("name")
        return render(request,'mainRecycleApp/home.html')

def populate_seed_data(request):
    '''Method to populate seed data for recycling centers in the recycling centers model'''
    if RecyclingCenter.objects.count() == 0:    
        RecyclingCenter(name = 'Vintage Thrift Gramercy', address = '286 3rd Avenue', recycleType = 'Household Furniture', borough = 'Manhattan', state = 'New York', zipcode='10010', phone='(212) 871-0777', picks_up='0', website='www.vintagethriftshop.org').save()
        RecyclingCenter(name = 'City Opera Thrift Shop', address = '222 East 23rd Street', recycleType = 'Household Furniture', borough = 'Manhattan', state = 'New York', zipcode='10010', phone='(212) 684-5344', picks_up='1', website='www.cityoperathriftshop.org', logo_url='https://i.imgur.com/1qh5hSQ.jpg').save()
        RecyclingCenter(name = 'The Salvation Army Of Greater New York', address = '208 E 23rd Street', recycleType = 'Household Furniture', borough = 'Manhattan', state = 'New York', zipcode='10010', phone='(800) 728-7825', picks_up='1', website='ny.salvationarmy.org/GreaterNewYork', logo_url='https://s3.amazonaws.com/cache.salvationarmy.org/resources/img/ihq-logo.jpg').save()
        RecyclingCenter(name = 'Housing Works', address = '157 East 23rd Street', recycleType = 'Household Furniture', borough = 'Manhattan', state = 'New York', zipcode='10010', phone='(347) 473-7400', picks_up='1', website='http://housingworks.org', logo_url='http://t2conline.com/wp-content/uploads/2016/03/Housing-Worls-2.jpg').save()
        RecyclingCenter(name = 'WPA', address = '347 East 10th Street', recycleType = '', borough = 'Manhattan', state = 'New York', zipcode='10009', phone='(646) 292-7740', picks_up='0').save()
        RecyclingCenter(name = 'Materials for the Arts', address = '33-00 Northern Blvd', recycleType = 'Electronics', borough = 'Queens', state = 'New York', zipcode='11101', phone='(718) 729-3001', picks_up='0', website='http://www.nyc.gov/html/dcla/mfta/html/home/home.shtml', logo_url='http://www.nyc.gov/html/dcla/mfta/includes/site_images/branding/logo.png').save()
        RecyclingCenter(name = 'Goodwill Industries of Greater New York & Northern New Jersey', address = '220 East 23rd Street', recycleType = 'Electronics', borough = 'Manhattan', state = 'New York', zipcode='10010', phone='(718) 728-5400', picks_up='1', website='http://goodwillnynj.org', logo_url='http://nycharityguide.org/img/logos/goodwillny.jpg').save()

"""
def search(request):
    '''Method to search from the database'''
    
    if request.method == 'GET':
        category = request.GET.getlist("gtype")
        day=request.GET.getlist("day")
        time = request.GET.getlist("dropdown")[0]
        zipcode = request.GET.getlist("zipcode")[0]
        db=sqlite3.connect("db.sqlite3")
        data = pd.read_sql_query("SELECT * FROM searchdb", db)
        db.close()
        bk = [10461, 10462,10464, 10465, 10472, 10473, 11209, 11214, 11228,11204, 11218, 11219, 11230, 11234, 11236, 11239,11223, 11224, 11229, 11235,11201, 11205, 11215, 11217, 11231,11203, 11210, 11225, 11226,11207, 11208,11211, 11222,11220, 11232,11206, 11221, 11237]
        mh = [10026, 10027, 10030, 10037, 10039,10001, 10011, 10018, 10019, 10020, 10036,10029, 10035,10010, 10016, 10017, 10022,10012, 10013, 10014,10004, 10005, 10006, 10007, 10038, 10280,10002,10003, 10009,10021, 10028, 10044, 10065, 10075, 10128,10023, 10024, 10025,10031, 10032, 10033, 10034, 10040]
        qn = [11361, 11362, 11363, 11364,11354, 11355, 11356, 11357, 11358, 11359, 11360,11365, 11366, 11367,11412, 11423, 11432, 11433, 11434, 11435, 11436,11101, 11102, 11103, 11104, 11105, 11106,11374, 11375, 11379, 11385,11691, 11692, 11693, 11694, 11695, 11697,11004, 11005, 11411, 11413, 11422, 11426, 11427, 11428, 11429,11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421,11368, 11369, 11370, 11372, 11373, 11377, 11378]
        
        borough=""
        if zip in bk:
            borough="Brooklyn"
        elif zip in mh:
            borough="Manhattan"
        else:
            borough = "Queens"
        result = []
        for i in range(0,len(category)):
            result.append(data.loc[data["type"]==category[i]])
        result = pd.concat(result)
        find = []
        for d in day:
            find.append(result.loc[result[d]!="closed"])
        result = pd.concat(find).drop_duplicates()
        checktime =[] 
        for d in day:
            checktime.append(result[d].values)
        index=[]
        for i in range(0,len(checktime[0])):
            for j in range(0,len(checktime)):
                if(checktime[j][i]=="closed"):
                    continue
                db_time=checktime[j][i].split(",")
                user_time=time.split(",")
                if int(db_time[0])<=int(user_time[0]) and int(db_time[1])>=int(user_time[1]):
                    index.append(i)
        index = list(set(index))
        result = result.iloc[index]
        """
        # return render(request,'mainRecycleApp/home.html', {"date":result})
    
