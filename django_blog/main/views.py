from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("<h1>testing home page</h1>")


def view2(response):
    return HttpResponse("<h1>testing 2nd page</h1>")

