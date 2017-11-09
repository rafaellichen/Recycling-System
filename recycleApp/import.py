import csv, sys, os

import django

django.setup()


direct = "/recycleApp/"

sys.path.append(direct)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from mainRecycleApp.models import RecycleCenter

data = csv.reader(open("DonateNYCCSV.csv"), delimiter=",")

for row in data:
	if row[0] != 'name':
		recycle = RecycleCenter()
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