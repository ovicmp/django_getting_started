from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the meeting Planner!")

def date(request):
    return HttpResponse("This page was served at " + str(datetime. now()))

def about(request):
    return HttpResponse("Welcome to the about page!")