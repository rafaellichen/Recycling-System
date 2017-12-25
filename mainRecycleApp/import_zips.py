"""Helper Import script to import the CSV data into the Django Zips Model"""
import csv

from mainRecycleApp.models import Zip

DATA = csv.reader(open("../static/data/zips.csv"), delimiter=",")

for row in DATA:
    zips = Zip()
    zips.zipcode = row[0]
    zips.state = row[1]
    zips.latitude = row[2]
    zips.longitude = row[3]
    zips.city = row[4]
    zips.save()
