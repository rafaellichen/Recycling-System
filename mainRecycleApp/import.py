"""Helper Import script to import the CSV data into the Django Models"""
import csv

from mainRecycleApp.models import RecyclingCenter

data = csv.reader(open("../static/data/DonateNYCCSV.csv"), delimiter=",")

for row in data:
    if row[0] != 'name':
        recycle = RecyclingCenter()
        recycle.name = row[0]
        recycle.address = row[1]
        recycle.monday = row[2]
        recycle.tuesday = row[3]
        recycle.wednesday = row[4]
        recycle.thrusday = row[5]
        recycle.friday = row[6]
        recycle.saturday = row[7]
        recycle.sunday = row[8]
        recycle.borough = row[9]
        recycle.state = row[10]
        recycle.zipcode = row[11]
        recycle.phone = row[12]
        recycle.picks_up = row[13]
        recycle.type = row[14]
        recycle.url = row[15]
        recycle.save()
