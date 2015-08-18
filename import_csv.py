dir = '/home/contes6/Documents/django/csvparse/mycsv.csv'

 
import sys,os
sys.path.append('/home/contes6/Documents/django/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] ='settings'

import settings

from models import getData
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
	
