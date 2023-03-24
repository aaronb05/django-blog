from django.shortcuts import render, redirect
import datetime as dt
from slugify import slugify
from .models import BlogPost
from .forms import CreatePost


def get_all_posts():
    all_posts = BlogPost.objects.all()
    return all_posts


def validate_slug(title):
    posts = get_all_posts()
    for post in posts:
        if title == post.Title:
            return False
        else:
            pass
    return True


def index(response):
    bp = get_all_posts().order_by("-Created")[:6]
    carousel = get_all_posts().order_by("-Created")[:3]
    return render(response, "main/index.html", {'blog_posts': bp, 'carousel': carousel})


def blog_post(response, slug):
    bp = BlogPost.objects.get(Slug=slug)
    return render(response, "main/post.html", {'post': bp})


def create_post(response):
    if response.method == "POST":
        form = CreatePost(response.POST)
        if form.is_valid():
            if validate_slug(form.cleaned_data["Title"]):
                bp = BlogPost()
                bp.Title = form.cleaned_data["Title"]
                bp.Description = form.cleaned_data["Description"]
                bp.Body = form.cleaned_data["Body"]
                bp.Slug = form.cleaned_data["Title"]
                bp.Published = False
                bp.Archived = False
                bp.Created = dt.datetime.now()
                bp.save()
                return redirect(f"/post/{bp.Slug}")
            else:
                error_message = "Error creating post, same title as previous post. Please select a new title!"
                render(response, "main/create_post.html", {"form": form}, {"error": error_message})
        else:
            error_message = f"Error creating post. Please check all inputs for errors"
            render(response, "main/create_post.html", {"form": form}, {"error": error_message})
    else:
        form = CreatePost()
        return render(response, "main/create_post.html", {"form": form})


