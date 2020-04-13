from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from datetime import date
# from datetime import today




# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()) )


def about(request):
   # return HttpResponse("I am Olawale. I'm glad to be alive today " + str(datetime.date.today()) )
    return HttpResponse("I am Olawale. I'm glad to be alive today " )
