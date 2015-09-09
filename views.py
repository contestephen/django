from django.shortcuts import render
from csvparse.models import getData
from django.http import HttpResponse

def csv(request):
	info=getData.objects.all()
	context = {'info': info}
	return render(request, 'csvparse/csv.html', context)

