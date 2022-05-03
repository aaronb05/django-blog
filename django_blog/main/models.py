from django.db import models

# Create your models here.


class BlogPost(models.Model):
    Id = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=200)
    Body = models.CharField(max_length=10000)
    Published = models.BooleanField()
    Archived = models.BooleanField()
    Created = models.DateTimeField(null=True)
    Updated = models.DateTimeField(null=True)

    # create hash set of comments
    # create collection of tags


class Comment(models.Model):
    Id = models.IntegerField(primary_key=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    Author = models.CharField(max_length=200)
    Body = models.CharField(max_length=1000)
    Created = models.DateTimeField()
    Updated = models.DateTimeField(null=True)

    # create virtual collection of blog posts
    # create virtual collection of Authors


