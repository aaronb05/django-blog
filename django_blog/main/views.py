from django.shortcuts import render
from django.http.response import HttpResponse
from .models import BlogPost, Comment


def index(response):
    return HttpResponse("<h1>testing home page</h1>")


def blog_post(response, id):
    bp = BlogPost.objects.get(Id=id)
    return HttpResponse("<h1>%s</h1>" %bp.Body)

