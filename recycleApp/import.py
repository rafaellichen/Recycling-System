'use if with django shell

import csv

from mainRecycleApp.models import RecycleCenter

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
		recycle.recycleType = row[7]
		recycle.website = row[8]
		recycle.save()