'''Helper Import script to import the CSV data into the Django Models'''
import csv

from mainRecycleApp.models import RecyclingCenter
from recycleApp import settings

data = csv.reader(open("DonateNYCCSV.csv"), delimiter=",")

for row in data:
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
