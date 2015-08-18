from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from pprint import pformat

class Command(BaseCommand):
    help = "Process CSV -- help test"
    option_list = BaseCommand.option_list + (
    )

    def handle(self, *args, **kwargs):
	dir = '/home/contes6/Documents/django/csvparse/mycsv.csv'
	 
	from csvparse.models import getData
	import csv

	reader = csv.reader(open(dir), delimiter=',', quotechar='"')
	for rownum, row in enumerate(reader):
		if rownum == 0:
			continue

		print "Processing row %s" % rownum

		if row[0] != 'Account':
			# create an intance of getData object
			mydict = {
				'account_num': row[0],
				'name': row[1],
				'street_address': row[2],
				'city': row[3],
				'state': row[4],
				'zipcode': row[5],
			}

			print mydict
			print pformat(mydict)


			mygetData = getData(**mydict)

			"""
			mygetData.account_num = row[0]
			mygetData.name = row[1]
			mygetData.street_address = row[2]
			mygetData.city = row[3]
			mygetData.state = row[4]
			mygetData.zipcode = row[5]
			"""

			# save
			mygetData.save()

			print "Inserted with Primary Key %s" % mygetData.pk
		
	 
