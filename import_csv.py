dir = 'home/contes6/Documents/django/csvparse/mycsv.csv'
djangoDir = '/home/contes6/Documents/django/mysite'

import sys,os
sys.path.append(djangoDir)
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'
  
dir = 'home/contes6/Documents/django/csvparse'
djangoDir = '/home/contes6/Documents/django'

import models.py
import csv

reader = csv.reader(open(dir), delimiter=',', quotechar='"')
for row in reader:
	if row[0] != 'Account':
		getData.account_num = row[0]
		getData.name = row[1]
		getData.street_address = row[2]
		getData.city = row[3]
		getData.state = row[4]
		getData.zipcode = row[5]
		getData.save()
	
