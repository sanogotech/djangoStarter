from django.shortcuts import render

# Create your views here.
# import Http Response from django 
from django.http import HttpResponse 
# get datetime 
import datetime 

# create a function 
def homecontact_view(request): 
	# fetch date and time 
	now = datetime.datetime.now() 
	# convert to string 
	html = "Time is {}".format(now) 
	# return response 
	return HttpResponse(html) 


def index(request):
    return HttpResponse("Hello, world. You're at the contactmanager index.")
