"""Helper Import script to import the CSV data into the Django Public Recycle Bins Model"""

import csv

from mainRecycleApp.models import PublicRecyclingBin

data = csv.reader(open("../static/data/publicbins.csv"), delimiter=",")

for row in data:
	bins = PublicRecyclingBin()
	bins.borough = row[0]
	bins.siteType = row[1]
	bins.siteName = row[2]
	bins.address = row[3]
	bins.latitude = row[4]
	bins.longitude = row[5]
	bins.save()
