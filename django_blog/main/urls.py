
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<slug>", views.blog_post, name="blog_post2"),
    path("create-post/", views.create_post, name="create-post"),
]

