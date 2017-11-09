import csv
import sys
import os
import django
from mainRecycleApp.models import RecyclingCenter

django.setup()

directory = "/recycleApp/"

sys.path.append(directory)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

csvData = csv.reader(open("DonateNYCCSV.csv"), delimiter=",")

for row in csvData:
    if row[0] != 'name':
        recycle = RecyclingCenter()
        recycle.name = row[0]
        recycle.address = row[1]
        recycle.borough = row[2]
        recycle.state = row[3]
        recycle.zipcode = row[4]
        recycle.phone = row[5]
        recycle.picks_up = row[6]
        recycle.type = row[7]
        recycle.url = row[8]
        recycle.save()
