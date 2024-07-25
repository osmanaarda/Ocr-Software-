from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index ():
     return HttpResponse("home page")

def blog():
     return HttpResponse("bloog syafası")



