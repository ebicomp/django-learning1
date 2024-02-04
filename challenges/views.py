from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def monthly_challenges(request,month):
    return render(request,"challenges/challenge.html")

def index():
    return HttpResponse