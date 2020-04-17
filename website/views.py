from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from datetime import date
# from datetime import today
from meetings.models import Meeting



# Create your views here.

# def welcome(request):
#     return HttpResponse("Welcome to the Meeting Planner")

def welcome(request):
    return render(request, "website/welcome.html", {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
   # return HttpResponse("I am Olawale. I'm glad to be alive today " + str(datetime.date.today()) )
    return HttpResponse("I am Olawale. I'm glad to be alive today " )
