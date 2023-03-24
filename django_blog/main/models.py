from django.db import models
from datetime import datetime


class BlogPost(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Title = models.CharField(max_length=200)
    Description = models.CharField(max_length=500, null=True)
    Body = models.TextField(max_length=10000)
    Slug = models.SlugField(max_length=250, unique=True)
    Published = models.BooleanField()
    Archived = models.BooleanField()
    Created = models.DateTimeField(default=datetime.now())
    Updated = models.DateTimeField(null=True)

    # create hash set of comments
    # create collection of tags


class Comment(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Author = models.CharField(max_length=200)
    Body = models.CharField(max_length=1000)
    Created = models.DateTimeField()
    Updated = models.DateTimeField(null=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    # create virtual collection of blog posts
    # create virtual collection of Authors


class Tags(models.Model):
    Id = models.IntegerField(primary_key=True, unique=True)
    Name = models.CharField(max_length=20, unique=True)
    Description = models.CharField(max_length=50)
    BlogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
