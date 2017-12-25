# -*- coding: utf-8 -*-
'''Views for mainRecycleApp'''
from __future__ import unicode_literals
from collections import OrderedDict
from mainRecycleApp.models import RecyclingCenter, SpecialWasteSite, Event, Zip, PublicRecyclingBin, Description
from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder

from math import sin, cos, sqrt, atan2, radians, acos
import geopy

# Create your views here.
def index(request):
    """
    This Method renders the home.html for route ('/')

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template mainRecycleApp/home.html being sent over
    """
    return render(request, 'mainRecycleApp/home.html')

def about(request):
    """
    This method renders the about.html for route ('/about') 

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template mainRecycleApp/about.html being sent over
    """
    return render(request, 'mainRecycleApp/about.html')

def contact(request):
    """
    This method renders the contact.html for route ('/contact')

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template mainRecycleApp/contact.html being sent over
    """
    return render(request, 'mainRecycleApp/contact.html')

def faqs(request):
    """
    This method renders the faqs.html for route ('/faqs')

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template mainRecycleApp/faqs.html being sent over
    """
    return render(request, 'mainRecycleApp/faqs.html')

def get_borough_from_zip(zipcode):
    """
    Converts the zipcode into the Borough name and returns it

    **Args:**
        zipcode: (int) Zipcode value any zipcode within NYC

    **Returns:**
        borough: (string) Borough name of all boroughs in NYC.
                 Value is empty if the zipcode is invalid or not of New York City
    """
    try:
        zip_code = int(zipcode)
    except ValueError:
        borough = ""
        return borough
        
    bk = [10461, 10462, 10464, 10465, 10472, 10473, 11209, 11214, 11228, 11204, 11218, 11219, 11230, 11234, 11236, 11239, 11223, 11224, 11229, 11235, 11201, 11205, 11215, 11217, 11231, 11203, 11210, 11225, 11226, 11207, 11208, 11211, 11222, 11220, 11232, 11206, 11221, 11237]
    mh = [10026, 10027, 10030, 10037, 10039,10001, 10011, 10018, 10019, 10020, 10036, 10029, 10035, 10010, 10016, 10017, 10022, 10012, 10013, 10014, 10004, 10005, 10006, 10007, 10038, 10280, 10002, 10003, 10009, 10021, 10028, 10044, 10065, 10075, 10128, 10023, 10024, 10025, 10031, 10032, 10033, 10034, 10040]
    qn = [11361, 11362, 11363, 11364, 11354, 11355, 11356, 11357, 11358, 11359, 11360, 11365, 11366, 11367, 11412, 11423, 11432, 11433, 11434, 11435, 11436, 11101, 11102, 11103, 11104, 11105, 11106, 11374, 11375, 11379, 11385, 11691, 11692, 11693, 11694, 11695, 11697, 11004, 11005, 11411, 11413, 11422, 11426, 11427, 11428, 11429, 11414, 11415, 11416, 11417, 11418, 11419, 11420, 11421, 11368, 11369, 11370, 11372, 11373, 11377, 11378]
    si = [10302, 10303, 10310, 10306, 10307, 10308, 10309, 10312, 10301, 10304, 10305, 10314]
    borough = ""
    if zip_code in bk:
        borough = "Brooklyn"
    elif zip_code in mh:
        borough = "Manhattan"
    elif zip_code in qn:
        borough = "Queens"
    elif zip_code in si:
        borough = "Staten Island"
    else:
        # Not a new york city zip code
        borough = ""
    return borough

def filter_day(result, day):
    """ 
    Filters the donation sites that has closed on the day the user chose

    **Args:**
        result: (List) list of donation site objects
        day: (List) list of days from Monday to Sunday

    **Returns:**
        filter_day: (List) List of new donation sites with filtered sites that are closed on day list
    """
    filter_out_day = []
    for e in result:
        for i in day:
            if e[i] != "closed":
                filter_out_day.append(e)
    return [dict(t) for t in set([tuple(d.items()) for d in filter_out_day])]

def filter_time(result, day, time):
    """ 
    Filter out facilities that don't match user's avaiable time

    **Args:**
        result: (List) list of donation site objects
        day: (List) list of days from Monday to Sunday
        time: (string) time selected by the user

    **Returns:**
        result: (List) List of new donation sites with filtered sites with time
    """
    checktime = []
    for d in day:
        temp = []
        for e in result:
            temp.append(e[d])
        checktime.append(temp)
    index = []
    for i in range(0,len(checktime[0])):
        for j in range(0,len(checktime)):
            if(checktime[j][i] == "closed"):
                continue
            db_time = checktime[j][i].split(",")
            user_time = time.split(",")
            if int(db_time[0]) <= int(user_time[0]) and int(db_time[1]) >= int(user_time[1]):
                index.append(i)
    # Remove duplicates in the result
    set_index = list(set(index))
    return [result[i] for i in set_index]

def get_special_waste_site(borough):
    """ 
    Method to get the special waste site
    Since there are only 4 special waste sites as of now, Location is stored as the borough name

    **Args:**
         borough: (string) Borough name within NYC.

    **Returns:**
        result: (string) Obtained from a json.dumps which converts the object into string
    """
    result_list = list(SpecialWasteSite.objects.filter(location=borough).values())
    if result_list  is not None:
        result = json.dumps(result_list, cls=DjangoJSONEncoder)
        return result

def get_safe_disposal_events():
    """ 
    Method to get the safe disposal events
    Returns the query result based on the borough input (boro)

    **Args:**
        boro: (string) Borough name within NYC.

    **Returns:**
        result: (string) Obtained from a json.dumps which converts the object into string
    """
    result = list(Event.objects.all().values())
    if result is not None:
        return result

def get_public_recycle_bins(boro):
    """ 
    Method to get the public recycle bins from the borough
    Returns the query result based on the borough input (boro)
    Capped the returned result to 10 elements for the MVP

    **Args:**
        boro: (string) Borough name within NYC.

    **Returns:**
        allresult: (string) Obtained from a json.dumps which converts the object into string
    """
    result = []
    all_result = list(PublicRecyclingBin.objects.filter(borough=boro).values()[:10])
    all_result = json.dumps(all_result, cls=DjangoJSONEncoder)
    return all_result

def return_lat_long_from_Zip(zip):
    """ 
    This method will return the latitude and longitude form Zipcode
    Note: Future improvement to pin-point the returned result, not currently in use for the MVP
    **Args:**
        zip: (int) Any Zipcode within New York State

    **Returns:**
        lat: (float) Obtained latitude from the query result
        lon: (float) Obtained longitude from the query result
    """
    result = list(Zip.objects.filter(zipcode=zip).values())
    lat = result[0]['latitude'].replace('"', '').strip()
    lon = result[0]['longitude'].replace('"', '').strip()
    lat = float(lat)
    lon = float(lon)
    return lat, lon


def check_Distance_Of_Zips(zip1, zip2):
    """ 
    Get the distance between two zipcodes
    Using the Haversine formula

    Note: Future improvement to pin-point the returned result, not currently in use for the MVP
    **Args:**
        zip1: (int) Any Zipcode within New York State
        zip2: (int) Any Zipcode within New York State

    **Returns:**
        float value : distance obtained from Haversine formula
    """
    lat1, long1 = return_lat_long_from_Zip(zip1)
    lat2, long2 = return_lat_long_from_Zip(zip2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    d_long = radians(long1 - long2)
    cosx = (sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(d_long))
    return acos(cosx) * 3958.761


def get_recommended_list(returnval, category):
    """
    Method to get the recommended list
    We are taking the returnval from our search with query and the categories that
    the user entered.
    
    **Args:**
        returnval: (list) list of donation sites objects
        category: (list) list of categories string
    
    **Returns:**
        returnval: (list) list of donation sites objects the recommended sites containing recommendedStatus
    """
    # Maintain a new list of found categories in the returnval
    filter_types = []
    recommended = []
    min_difference = 0
    # loop through each item in the returnval
    for item in returnval:
        # Loop through each sub category
        for category_type in item["type"]:
            for cat_type in category:
                if category_type == cat_type:
                    # there is a match
                    if cat_type not in filter_types:
                        # if it is not already in filter_types append it
                        filter_types.append(category_type)
                        # if the item is not already in recommened add it
                        if item not in recommended:
                            # Also need to check for zipcode variance before adding to recommended
                            recommended.append(item)
                            # Remove the items from the returnval
                            returnval.remove(item)
    """
    Loop through the list in reverse since we know that the returnval is arranged by
    len, ideally a different recommended list should be passed, however we added this
    for testing our proof of concept
    """
    for item in reversed(recommended):
        item["recommendedStatus"] = "true"
        returnval.insert(0, item)
    return returnval

def get_further_details(name):
    """
    Method to get the details of the donation sites
    **Args:**
        name: (string) Name of the donation site

    **Returns:**
        further_desc: (object) Query result for further desc based on the user input 'name'
    """
    further_desc = Description.objects.filter(name=name).values()
    # print (further_desc)
    return further_desc

def donationSiteDetails(request, id):
    """
    This method renders the donationSites.html for route ('/donation/<id>')
    
    Querying RecyclingCenter model based on the 'idc' attribute which will return all the
    donation centers that have this idc

    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template mainRecycleApp/donationSites.html being sent over
    """
    result = RecyclingCenter.objects.filter(idc=id).values()
    final = combine_idc(result)
    # print(final) 
    for i in final:
        final[i]["type"] = final[i]['type'].split(",")
    # print (final)
    final = parse_time_table(final)
    returnval = []
    for i in final:
        returnval.append(final[i])
    returnDesc = get_further_details(returnval[0]['name'])
    return render(request, 'mainRecycleApp/donationSites.html', {"donationSite" : returnval[0],
                                                                 "furtherInfo" : returnDesc})

def parse_time_table(final):
    """
    Method to parse the time from eg 1000,2000 to 10:00 - 20:00 string format
    **Args:**
        final: (list) list of donation site objects

    **Returns:**
        final: (list) Modified list of donation site objects
    """
    for i in final:
        if final[i]["Monday"] != "closed":
            temp = final[i]["Monday"].split(",")
            final[i]['Monday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
        if final[i]["Tuesday"] != "closed":
            temp = final[i]["Tuesday"].split(",")
            final[i]['Tuesday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
        if final[i]["Wednesday"] != "closed":
            temp = final[i]["Wednesday"].split(",")
            final[i]['Wednesday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
        if final[i]["Thursday"] != "closed":
            temp = final[i]["Thursday"].split(",")
            final[i]['Thursday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
        if final[i]["Friday"] != "closed":
            temp = final[i]["Friday"].split(",")
            final[i]['Friday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
        if final[i]["Saturday"] != "closed":
            temp = final[i]["Saturday"].split(",")
            final[i]['Saturday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
        if final[i]["Sunday"] != "closed":
            temp = final[i]["Sunday"].split(",")
            final[i]['Sunday'] = temp[0][0:2]+":"+temp[0][2:]+" - "+temp[1][0:2]+":"+temp[1][2:]
    return final

def combine_idc(result):
    """
    Method to combine the result of several donation site into one
    Note: This was an quick solution proposed and completed by the team for this MVP.
    Changes in models in later version will help remove this method altogether

    **Args:**
        result: (list) list of donation site objects
    **Returns:**
        final: (list) Combined donation site object with all recycle types in one list of 'type'
    """
    final = {}
    for cur_element in result:
        keys = (cur_element["idc"])
        if keys in final:  # combine when have same "idc"
            final[keys] = {"idc":cur_element["idc"], 
                           "name": cur_element["name"],
                           "address": cur_element["address"],
                           "Monday": cur_element["Monday"],
                           "Tuesday": cur_element["Tuesday"],
                           "Wednesday": cur_element["Wednesday"],
                           "Thursday": cur_element["Thursday"],
                           "Friday": cur_element["Friday"],
                           "Saturday": cur_element["Saturday"],
                           "Sunday": cur_element["Sunday"],
                           "borough": cur_element["borough"],
                           "zip": cur_element["zip"],
                           "picksup": cur_element["picksup"],
                           "cell":cur_element["cell"],
                           "url": cur_element["url"],
                           "type": cur_element["type"] + "," +final[keys]["type"]}
        else:  # for unique "idc"
            final[keys] = {"idc":cur_element["idc"],
                           "name": cur_element["name"], 
                           "address": cur_element["address"],
                           "Monday": cur_element["Monday"],
                           "Tuesday": cur_element["Tuesday"],
                           "Wednesday": cur_element["Wednesday"],
                           "Thursday": cur_element["Thursday"],
                           "Friday": cur_element["Friday"],
                           "Saturday": cur_element["Saturday"],
                           "Sunday": cur_element["Sunday"],
                           "borough": cur_element["borough"],
                           "zip": cur_element["zip"],
                           "picksup": cur_element["picksup"],
                           "cell":cur_element["cell"],
                           "url": cur_element["url"],
                           "type": cur_element["type"]}
    return final


def search_withQuery(request):
    '''Method to search with query from the database'''
    """
    This Method renders the home.html for route ('/search') 
    **Args:**
        request: HttpRequest object created by Django

    **Returns:**
        render: HttpResponse object with the template mainRecycleApp/home.html being sent over 
        With context "data" : List of donation center object
                     "bookmarks" : List of bookmarks associated with the user
                     "userCategories" : List of categories that the user queried
                     "days" : List of days that user selected
                     "specialWasteSite" : String JSON of special waste sites
                     "safeDisposalEvents" : String JSON of safe disposal events
                     "publicRecycleBins" : String JSON of public recycle bins 
    """
    if request.method == 'POST':
        category = request.POST.getlist("gtype")
        day = request.POST.getlist("day")
        time = ""
        try:
            time = request.POST.getlist("dropdown")[0]
        except:
            time = ""
        zipcode = request.POST.getlist("zipcode")[0]
        borough = get_borough_from_zip(zipcode)
        if borough == "":
            return render(request, 'mainRecycleApp/home.html', {"data": [], "invalid": True})
        '''Filter list by user selected categories determined borough'''
        result = list(RecyclingCenter.objects.filter(type__in=category).filter(borough=borough).values())
        special_waste_site = get_special_waste_site(borough)
        safe_disposal_events = get_safe_disposal_events()
        public_recycle_bins = get_public_recycle_bins(borough)

        if(day != []):
            result = filter_day(result,day)
        if(time != ""):
            result = filter_time(result, day, time)
        final = combine_idc(result)
        for i in final:
            final[i]["type"] = final[i]['type'].split(",")
            final[i]["len"] = len(final[i]["type"])
        final = parse_time_table(final)
        final = OrderedDict(sorted(final.items(), key=lambda kv: kv[1]['len'], reverse=True))
        returnval = []
        for i in final:
            final[i]['long'] = 1
            final[i]['lat'] = 1
            returnval.append(final[i])
        # print (check_Distance_Of_Zips('11104', '10016'))
        get_recommended_list (returnval, category)
        bookmarks = []
        if request.user.is_authenticated:
            bookmarks = list(set(request.user.bookmarks.values_list('facility', flat=True)))

        return render(request, 'mainRecycleApp/home.html', {"data": returnval,
                                                            "bookmarks":bookmarks,
                                                            "userCategories": category,
                                                            "days": day,
                                                            "specialWasteSite" : special_waste_site,
                                                            "safeDisposalEvents" : safe_disposal_events,
                                                            "publicRecycleBins" : public_recycle_bins})
